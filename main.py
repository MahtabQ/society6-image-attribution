## This is the main entry point for the Society6 image processing pipeline.
## It orchestrates the downloading of images, processing them with a machine learning model,
## and post-processing the results to extract and clean up attributes.

import os
import sys
import pandas as pd
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv

try:
    # First the biger context (like pipeline/streamx try the relative import first)
    from .model.img_downloader import download_process
    from .model.model_pipeline import process_image, setup_vertex_ai
    from .model.stopwords_removal import process_file
    from .model.post_processing import process_template
except ImportError:
    # if relative import fails mean we are directly running main.py
    from model.img_downloader import download_process
    from model.model_pipeline import process_image, setup_vertex_ai
    from model.stopwords_removal import process_file
    from model.post_processing import process_template


# Configure logging
logging.basicConfig(
    filename="process.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def load_environment_config():
    """
    Load environment variables from the .env file in the model folder.
    Returns a dictionary with configuration values.
    """
    # Get the current directory and construct path to .env file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(current_dir, "model", "image_enrichment.env")
    
    # Load environment variables from the .env file
    if os.path.exists(env_path):
        load_dotenv(env_path)
        logging.info(f"Environment file loaded from: {env_path}")
    else:
        logging.warning(f"Environment file not found at: {env_path}")
        raise FileNotFoundError(f"Environment file not found: {env_path}")
    
    # Extract configuration values directly from environment (no fallbacks)
    required_configs = ['PROJECT_ID', 'LOCATION', 'MODEL_NAME', 'CREDENTIALS_FILE', 'MAX_WORKERS', 'MAX_TOKENS', 'MAX_RETRIES']
    
    config = {}
    missing_configs = []
    
    for key in required_configs:
        value = os.getenv(key)
        if value is None:
            missing_configs.append(key)
        else:
            # Convert numeric values to appropriate types
            if key in ['MAX_WORKERS', 'MAX_TOKENS', 'MAX_RETRIES']:
                try:
                    config[key.lower()] = int(value)
                except ValueError:
                    raise ValueError(f"Invalid numeric value for {key}: {value}")
            else:
                config[key.lower()] = value
    
    if missing_configs:
        raise ValueError(f"Missing required configuration values in .env file: {', '.join(missing_configs)}")
    
    logging.info(f"Configuration loaded: {config}")
    return config


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python code.py <input_csv>")
        

    # arguments for input file csv and output folder path as image_path
    input_file = sys.argv[1]
    image_path = sys.argv[2]

    # Validate arguments
    if not input_file:
        print("Error: <input_file> is mandatory.")
        sys.exit(1)

    try:
        # Load configuration from environment file
        config = load_environment_config()
        
        # Extract configuration values
        project_id = config['project_id']
        location = config['location']
        model_name = config['model_name']
        credentials_file = config['credentials_file']
        max_workers = config['max_workers']
        max_retries = config['max_retries']
        max_tokens = config['max_tokens']
        
        # Construct credentials path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        creds_path = os.path.join(current_dir, credentials_file)
        
        # Validate credentials file exists
        if not os.path.exists(creds_path):
            logging.error(f"Credentials file not found: {creds_path}")
            print(f"Error: Credentials file not found: {creds_path}")
            sys.exit(1)
        
        print(f"Using configuration - Project: {project_id}, Location: {location}, Model: {model_name}")
        
    except Exception as e:
        logging.error(f"Error loading configuration: {e}")
        print(f"Error loading configuration: {e}")
        sys.exit(1)

    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cax-poc-7585d859d15a.json"
    downloaded_image_path = download_process(input_file, image_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_folder = os.path.join(script_dir, downloaded_image_path)
    print("Image folder:", image_folder)

    files = [f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".png", ".jpeg", ".webp"))]
    if not files:
        raise FileNotFoundError(f"No images found in {image_folder}")

    # downloaded_image_path should be the folder, not a single image:
    print("Using image folder as base path:", downloaded_image_path)

    try:
        # Initialize Vertex AI with configuration from .env file
        llm = setup_vertex_ai(project_id, creds_path, location, model_name)

        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(input_file)

        # Prepare a list to store results
        results = []
        total_images = len(df)

        # Define the function to process a single row
        def process_row(row):
            sku_id = row['SKU_ID']
            raw_name = str(row['Name'])
            image_name = str(row['IMAGE_NAME'])
            url = row['URL']
            name = raw_name if raw_name.lower().endswith('.jpg') else f"{raw_name}.jpg"
            full_image_path = os.path.join(downloaded_image_path, name)

            if not os.path.exists(full_image_path):
                logging.warning(f"Image file not found while processing the images using csv file: {full_image_path}")
                return [sku_id, name, image_name, url, None, None, None, None, None, None]

            image_attributes,input_tokens, output_tokens  = process_image(full_image_path, llm)

            if image_attributes and input_tokens and output_tokens:
                return [
                    sku_id, name, image_name, url,
                    image_attributes.get('Medium'),
                    image_attributes.get('Style'),
                    image_attributes.get('Subject'),
                    image_attributes.get('Pattern'),
                    image_attributes.get('Color'),
                    image_attributes.get('Keyword'),
                    input_tokens,
                    output_tokens
                ]
            else:
                logging.info(f"Image attributes or tokens not found for SKU ID: {sku_id}, Image Name: {name}")
                return [sku_id, name, image_name, url, None, None, None, None, None, None, None, None]
    
        # Use ThreadPoolExecutor to process rows in parallel with configurable max_workers
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(process_row, row) for _, row in df.iterrows()]
            for i, future in enumerate(as_completed(futures), 1):
                result = future.result()
                results.append(result)
                percent = (i / total_images) * 100
                print(f"Processed {i}/{total_images} images ({percent:.2f}%)")

        # Create a new DataFrame from the results
        results_df = pd.DataFrame(results, columns=[
            'SKU_ID', 'Name','IMAGE_NAME', 'URL',
            'Medium', 'Style', 'Subject', 'Pattern', 'Color', 'Keyword', 'input_tokens','output_tokens'
        ])

        # Save the DataFrame to a new CSV file
        output_csv = os.path.join(downloaded_image_path, "society6_gemini_2-5_flash_results.csv")
        results_df.to_csv(output_csv, index=False)
        print(f"initial Results saved in file: {output_csv}")
        logging.info(f"Analysis Completed, results before post processing saved in: {output_csv}")

        df_excl_excess = process_file(results_df,downloaded_image_path)
        filename_no_ext = os.path.splitext(os.path.basename(output_csv))[0]
        output_csv_path = os.path.join(downloaded_image_path, f"{filename_no_ext}_cleaned.csv")
        output_excel_path = os.path.join(downloaded_image_path, f"{filename_no_ext}_cleaned.xlsx")
        
        df_excl_excess.to_csv(output_csv_path, index=False)
        df_excl_excess.to_excel(output_excel_path, index=False)
        print(f"Saved cleaned CSV to: {output_csv_path}")
        print(f"Saved cleaned Excel to: {output_excel_path}")
        logging.info(f"Analysis Completed, results after post processing saved in: {output_csv_path}")

        process_template(df_excl_excess,downloaded_image_path)

    except Exception as e:
        logging.error(f"Error in main execution: {e}")
        print(f"Error in main execution: {e}")
        
