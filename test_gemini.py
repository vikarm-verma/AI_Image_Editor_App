# Import the os module to read environment variables.
import os

# Import load_dotenv to load variables from the .env file.
from dotenv import load_dotenv

# Import the Gemini API client.
from google import genai

# Import PIL Image to open and handle the image file.
from PIL import Image


# Load the variables stored in the .env file.
load_dotenv()


# Read the Gemini API key from the environment variable.
api_key = os.getenv("GEMINI_API_KEY")


# Create a Gemini API client using the API key.
client = genai.Client(api_key=api_key)


# Open the input image using Pillow.
image = Image.open("test_image.png")


# Send the editing instruction and image to Gemini.
response = client.models.generate_content(
    
    # Specify the Gemini image editing model.
    model="gemini-3.1-flash-image",

    # Provide the editing instruction and the input image.
    contents=[
        "Make the photo look more professional. Improve the lighting and overall appearance.",
        image
    ]
)


# Go through each part of Gemini's response.
for part in response.parts:

    # Check whether Gemini returned an image.
    if part.inline_data is not None:

        # Convert the returned image data into a PIL image.
        edited_image = part.as_image()

        # Save the edited image as a PNG file.
        edited_image.save("edited_test.png")

        # Confirm that the editing process was successful.
        print("Image editing completed!")

        # Tell us where the edited image was saved.
        print("Saved as edited_test.png")