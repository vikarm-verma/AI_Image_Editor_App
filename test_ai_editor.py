# Import the image editing function from our AI editor module.
from ai_editor import edit_image

# Import PIL Image to open the test image.
from PIL import Image


# Open the test image from the project folder.
image = Image.open("test_image.png")


# Define the instruction that we want Gemini to apply.
prompt = "Improve the lighting and make this photo look more professional."


# Send the image and prompt to our AI editing function.
edited_image = edit_image(image, prompt)


# Check whether an edited image was returned.
if edited_image:

    # Save the edited image as a new file.
    edited_image.save("edited_from_function.png")

    # Confirm that the editing was successful.
    print("AI image editing completed successfully!")

    # Display the output file name.
    print("Saved as edited_from_function.png")

else:

    # Display an error message if no image was returned.
    print("No edited image was returned.")