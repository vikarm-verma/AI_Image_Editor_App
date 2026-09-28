# Import os to read environment variables.
import os

# Import BytesIO to convert image bytes into a file-like object.
from io import BytesIO

# Import load_dotenv to load the API key from the .env file.
from dotenv import load_dotenv

# Import the Gemini API client.
from google import genai

# Import PIL Image to work with image files.
from PIL import Image


# Load the variables stored in the .env file.
load_dotenv()


# Read the Gemini API key from the environment.
api_key = os.getenv("GEMINI_API_KEY")


# Create the Gemini API client using the API key.
client = genai.Client(api_key=api_key)


# Define a function that receives an image and an editing instruction.
def edit_image(image, prompt):

    # Send the editing instruction and image to the Gemini image model.
    response = client.models.generate_content(

        # Specify the Gemini image editing model.
        model="gemini-3.1-flash-image",

        # Provide the user's instruction and the input image.
        contents=[
            prompt,
            image
        ]
    )

    # Check every part of Gemini's response.
    for part in response.parts:

        # Check whether Gemini returned image data.
        if part.inline_data is not None:

            # Get the raw image bytes returned by Gemini.
            image_bytes = part.inline_data.data

            # Convert the raw bytes into a PIL image.
            edited_image = Image.open(
                BytesIO(image_bytes)
            ).copy()

            # Explicitly set the image format to PNG.
            edited_image.format = "PNG"

            # Return the properly formatted PIL image.
            return edited_image

    # Return None if Gemini did not return an image.
    return None