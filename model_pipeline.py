## This is the model pipeline script for Society6 image attributes extraction.
## It handles the setup of the Vertex AI client, image encoding, message preparation,
## and invoking the LLM to get structured responses for various image attributes.

import os
import base64
import logging
import json
from langchain_core.messages import HumanMessage
from langchain_google_vertexai import ChatVertexAI

try:
    # First the biger context (like pipeline/streamx try the relative import first)
    from ..model.attribute_def import subject_def, medium_def, pattern_def, style_def, color_def, Keywords_def
    from .model.attribute_def import subject_def, medium_def, pattern_def, style_def, color_def, Keywords_def
except ImportError:
    # if relative import fails mean we are directly running main.py
    from model.attribute_def import subject_def, medium_def, pattern_def, style_def, color_def, Keywords_def


def setup_vertex_ai(project_id: str, creds_path: str, location: str, model_name: str) -> ChatVertexAI:
    """
    Sets up and initializes the Vertex AI client.
    """
    # Validate credentials file exists
    if not os.path.exists(creds_path):
        raise FileNotFoundError(f"Credentials file not found: {creds_path}")
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds_path
    
    # Optionally verify the credentials work
    try:
        logging.info(f"Using credentials from: {creds_path}")
        return ChatVertexAI(model=model_name, project_id=project_id, region=location, temperature=0, max_token = 30000, max_retries = 10)
    except Exception as e:
        logging.error(f"Failed to initialize Vertex AI with provided credentials: {e}")
        raise


# Function to encode an image to Base64
def encode_image(image_path: str) -> str:
    """
    Encodes the given image file to a Base64 string.
    Args:
        image_path: Path to the image file.
    Returns:
        Base64-encoded string of the image.
    Raises:
        FileNotFoundError: If the image file is not found.
        Exception: For other unforeseen errors.
    """
    try:
        with open(image_path, "rb") as image_file:
            logging.info(f"Encoding image: {image_path}")
            return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        logging.error(f"Image file not found: {image_path}")
        raise
    except Exception as e:
        logging.error(f"Error encoding image: {image_path}. Details: {e}")
        raise


# Function to prepare dynamic messages for multiple attributes
def prepare_messages(image_base64: str) -> HumanMessage:
    """
    Prepares the HumanMessage payload with queries for multiple attributes. 
    """
    try:
        attributes_with_definition = {
            "medium_def": medium_def,
            "style_def": style_def,
            "subject_def": subject_def,
            "pattern_def": pattern_def,
            "color_def": color_def,
            "Keywords_def": Keywords_def
        }

        current_directory = "examples"

        example_images = {
            "example_1": os.path.join(current_directory, "ikat.jpg"),
            "example_2": os.path.join(current_directory, "tie_dyed.jpg"),
        }

        # Encode example images
        encoded_examples = {
            key: encode_image(path) for key, path in example_images.items()
        }

        # Prompt instructions
        prompt_instructions = (
            "You are an expert art image attribution analyst. You have to analyze the images belonging from art.com website.\n"
            "Please analyze the following artwork, graphic design, photography, typography, collage and provide results for the following attributes:\n"

            '"Medium options": [{"Collage","Drawing","Graphic Design","Illustration","Painting","Photography","Typography","Vector Art", "None"}]'
            
            '"Style options": [{"Abstract","Antique","Anime","Art Deco","Art Nouveau","Boho","Cabin","Cartoon","Coastal","Contemporary","Eclectic","Farmhouse","Figurative","Folk Art","Geometric","Glam","Impressionism","Mid-Century Modern","Minimalism","Modern","Nautical","Pop Art","Psychedelic","Retro","Scandinavian","Surrealism","Street Art","Traditional","Victorian","Vintage","Watercolor"}]'

            '"Subject options": [{"Abstract","Animals","Architecture","Astrology","Cocktails","Desert","Flowers","Food","Forest","Funny","Inspirational","Kids","Landscape","LGBTQ","Lines","Mountains","Music","Nature","Ocean","Space","Plants","Portraits","Rainbows","Shapes","Sports","Still Life","Travel","Tropical","Western","Typography"}]'
            
            '"Pattern options": [{"Animal Print","Botanical","Checks","Chevron","Geometric","Ikat","Tie-Dyed","Floral","Marble","Ombre","Dots","Plaid","Solid","Stripes","Swirl", "None"}]'

            '"Color options": [{"Red","Orange","Peach","Yellow","Avocado","Green","Sage","Teal","Cyan","Blue","Navy","Purple","Magenta","Pink","Beige","Brown","Grey","Black","White","Multicolor"}]'

            '"Keyword": ["Provide upto 20 keywords only in english language based on the image as {"keyword1", "keyword2", "keyword3", ...}]"]'

            "Ensure each classification category is mutually exclusive (no overlapping classifications) and collectively exhaustive (every image must fit clearly into one category):\n"

            "\nFor each of the following attributes (Medium, Style, Subject, Pattern, Color), please predict the top 5 most confident values (or fewer if not enough meet criteria) with their confidence scores that are greater than 70 out of 100 (in absolute values, e.g., 85 instead of .85).\n"
            "\nFor the Attributes like Medium, Style, Subject, Pattern and Color, predict the value and its confidence, upto top 5 most confident values are accepted."
            "Please keep the predicted values as per the decreasing order of confidence. ONLY include predictions with a confidence score greater than 70%.\n"
            "Return your response in the exact JSON format as follows:\n\n"
            "{\n"
            '  "Medium": [{"value": "...", "confidence": ..., "value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,}],\n'
            '  "Style": [{"value": "...", "confidence": ..., "value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,}],\n'
            '  "Subject": [{"value": "...", "confidence": ..., "value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,}],\n'
            '  "Pattern": [{"value": "...", "confidence": ..., "value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,}],\n'
            '  "Color": [{"value": "...", "confidence": ..., "value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,}],\n'
            '  "Keyword": [{"value": "...", "confidence": ..., "value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,"value": "...", "confidence": ...,}]\n'
            "}\n\n"
            "Respond only in this JSON format.\n"
        )

        # Build message content list
        message_content = []
        
        # Add main prompt text
        message_content.append({
            "type": "text",
            "text": prompt_instructions
        })

        # Added example 1
        message_content.append({
            "type": "text",
            "text": "EXAMPLE 1 - example of pattern as Ikat:"
        })
        message_content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{encoded_examples['example_1']}"}
        })
        message_content.append({
            "type": "text",
            "text": """In this example, the pattern is Ikat:\n
                    "Pattern": "Ikat"
                    """
        })

        # Added example 2
        message_content.append({
            "type": "text",
            "text": "EXAMPLE 2 - example of pattern as Tie-Dyed:"
        })
        message_content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{encoded_examples['example_2']}"}
        })
        message_content.append({
            "type": "text",
            "text": """In this example, the pattern is Tie-Dyed:\n
                    "Pattern": "Tie-Dyed"
                    """
        })

        # Add attribute definitions
        for attribute, attr_definition in attributes_with_definition.items():
            message_content.append({
                "type": "text",
                "text": f"\n{attr_definition}."
            })

        # Add the main image to analyze
        message_content.append({
            "type": "text",
            "text": "Now analyze this image:"
        })
        message_content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}
        })

        logging.info("Prepared messages for LLM with image and instructions.")

        return HumanMessage(content=message_content)
    except Exception as e:
        logging.error(f"Error preparing messages for LLM: {e}")
        raise

# Function to invoke the LLM
def get_llm_response(llm: ChatVertexAI, message: HumanMessage) -> dict:
    """
    Invokes the LLM with the given message and retrieves the response.
    """
    try:
        response = llm.invoke([message])
        # print(response)
        logging.info("LLM response received successfully.")

        # Extract token usage
        usage_metadata = response.usage_metadata
        # print("usage_metadata", usage_metadata)
        input_tokens = usage_metadata.get('input_tokens')
        output_tokens = usage_metadata.get('output_tokens')
        return response.content, input_tokens, output_tokens # Expected to return structured output
    
    except Exception as e:
        logging.error(f"Error invoking LLM. Details: {e}. Skipping this image since max_token exceeded.")
        return "", None, None

def process_image(image_path, llm):
    """
    Processes a single image using the LLM to extract attributes.
    """
    try:
        # Encode image
        image_base64 = encode_image(image_path)

        # Prepare messages for multiple attributes
        message = prepare_messages(image_base64)

        # Get response from LLM
        response, input_tokens, output_tokens = get_llm_response(llm, message)

        start_idx = response.find('{')
        end_idx = response.rfind('}')  # Find last closing brace

        if start_idx != -1 and end_idx != -1 and start_idx < end_idx:
            json_string = response[start_idx:end_idx + 1]  # Extract JSON part
            try:
                structured_output = json.loads(json_string)  # Load JSON from extracted part
                logging.info(f"Successfully parsed JSON response: {structured_output}")
                return structured_output, input_tokens, output_tokens   # Return the structured output
            except json.JSONDecodeError:
                logging.error(f"Could not decode JSON string: {json_string}") #Log string, but keep going
                return None, None, None #Handle downstream by returning None
        else:
            logging.error(f"Could not find valid JSON delimiters in LLM response. Response was: {response}")
            return None, None, None 
        # ------------------ END ROBUST JSON PARSING ------------------
    except Exception as e:
        logging.error(f"Error processing image {image_path}: {e}")
        return None, None, None