## Post processing for template data from Society6 attribution results.
## This script processes the results from Society6 image attributes extraction,
## extracting values from lists of dictionaries, and saving them into CSV and Excel files.

import ast
import os
import logging
import pandas as pd

# Configure logging
logging.basicConfig(
    filename="process.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def extract_values(data_str, max_items=5, with_confidence=False):
    try:
        data_list = ast.literal_eval(str(data_str))
        if not isinstance(data_list, list):
            return [None] * max_items
    except (ValueError, SyntaxError):
        return [None] * max_items

    result = []
    for item in data_list[:max_items]:
        if isinstance(item, dict) and 'value' in item:
            val = item['value']
            if isinstance(val, str):
                val = val.title()  ## Convert to Title Case

            if with_confidence and 'confidence' in item:
                val = f"{val} | {item['confidence']}"
            result.append(val)
        else:
            result.append(None)

    while len(result) < max_items:
        result.append(None)
    return result

# Main processing function
def process_template(input_df, output_folder):
    try:
        # stopword_dict = load_stopwords()
        # df = pd.read_csv(input_path)

        column_specs = {
            "Medium": 5,
            "Style": 5,
            "Subject": 5,
            "Pattern": 5,
            "Color": 5,
            "Keyword": 20
        }

        static_columns = ['SKU_ID', 'Name','IMAGE_NAME', 'URL']
        df_csv = input_df[static_columns].copy()
        df_excel = input_df[static_columns].copy()

        os.makedirs(output_folder, exist_ok=True)

        for col, max_items in column_specs.items():
            if col not in input_df.columns:
                logging.warning(f"Column '{col}' not found in input.")
                continue

            output_cols = [f"{col}{i}" for i in range(1, max_items + 1)]

            # Extract raw and enriched (with confidence) lists
            base_extracted = input_df[col].apply(lambda x: extract_values(x, max_items, False)).tolist()
            enriched_extracted = input_df[col].apply(lambda x: extract_values(x, max_items, True)).tolist()


            # Assign to DataFrames
            df_csv[output_cols] = pd.DataFrame(base_extracted, index=input_df.index)
            df_excel[output_cols] = pd.DataFrame(enriched_extracted, index=input_df.index)
        
        # Drop 'Name' column if it exists
        for df in [df_csv, df_excel]:
            if 'Name' in df.columns:
                df.drop(columns=['Name'], inplace=True)

        # Output file paths
        base_name = "Societ6_Tagging_Results"


        csv_output = os.path.join(output_folder, f"{base_name}_Delivery_File.csv")
        excel_output1 = os.path.join(output_folder, f"{base_name}_Validation_File_Without_CS.xlsx")
        excel_output2 = os.path.join(output_folder, f"{base_name}_Validation_File_With_CS.xlsx")

        df_csv.to_csv(csv_output, index=False)
        df_csv.to_excel(excel_output1, index=False)
        df_excel.to_excel(excel_output2, index=False)

        print(f"\nCSV saved to: {csv_output}")
        print(f"Excel saved to: {excel_output1}")
        print(f"Excel saved to: {excel_output2}")
        
        logging.info(f"CSV saved to: {csv_output}")
        logging.info(f"Excel saved to: {excel_output1}")
        logging.info(f"Excel saved to: {excel_output2}")
        return df_csv, df_excel
    except Exception as e:
        logging.error(f"Error during processing: {str(e)}", exc_info=True)
        print(f"Error processing file: {e}")
