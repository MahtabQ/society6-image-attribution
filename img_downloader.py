## Image downloading and processing script for Society6 images.
## This script downloads images from provided URLs, converts them to JPG format if necessary,   
## and saves them in a specified directory. It uses multithreading to speed up the download process.
## It also includes error handling and logging for better traceability.


from math import e
import os
import requests
import logging
import pandas as pd
import threading
import uuid
from PIL import Image


# Configure logging
logging.basicConfig(
    filename="process.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def cvt2jpg_updated(img_path):
        """
        This Function intends to convert any type of image to jpg format
        """
        pil_img = Image.open(img_path)
        try:
            fill_color = (255,255,255)  # your new background color

            pil_img = pil_img.convert("RGBA")   # it had mode P after DL it from OP
            if pil_img.mode in ('RGBA', 'LA'):
                background = Image.new(pil_img.mode[:-1], pil_img.size, fill_color)
                background.paste(pil_img, pil_img.split()[-1]) # omit transparency
                pil_img = background

            pil_img = pil_img.convert("RGB")

            logging.info(f"Image converted as per the required resolution")

            return pil_img

        except Exception as e:
            logging.error(f"Error in converting image {img_path} to jpg format")
            return "non-image"

def download_image(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        with open(filename, 'wb') as file:
            file.write(response.content)
        filename = filename.replace(".png",'.jpg').replace('gif','.jpg').replace(".PNG",".jpg")
    
        cvt2jpg_updated(filename).save(filename)
        print(f"Downloaded: {filename}")
        logging.info(f"Downloaded: {filename}")

    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        logging.error(f"Error downloading {url}: {e}")



def download_images_multithreaded(rows, download_folder):
    os.makedirs(download_folder, exist_ok=True)
    threads = []
    for sku, name, url in rows:
        if not url:
            logging.warning(f"Skipping empty URL for SKU {sku}")
            continue
        safe_name = f"{name}.jpg"
        filename = os.path.join(download_folder, safe_name)
        thread = threading.Thread(target=download_image, args=(url, filename))
        threads.append(thread)
        thread.start()
    for t in threads:
        t.join()
    logging.info("All downloads complete")
    return download_folder

def download_process(input_file, download_path):
    unique_id = uuid.uuid4().hex
    download_folder = os.path.join(download_path, f"downloaded_files_{unique_id}")

    df = pd.read_csv(input_file)
    rows = df[["SKU_ID", "Name", "URL"]].itertuples(index=False, name=None)
    download_images_multithreaded(rows, download_folder)

    print("Images downloaded to:", download_folder)
    return download_folder