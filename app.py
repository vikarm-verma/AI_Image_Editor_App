# Import Streamlit to build the web application interface.
import streamlit as st

# Import BytesIO to convert the edited image into downloadable bytes.
from io import BytesIO

# Import the AI image editing function from our ai_editor module.
from ai_editor import edit_image

# Import PIL Image to open and handle uploaded images.
from PIL import Image


# Configure the Streamlit page settings.
st.set_page_config(
    page_title="AI Photo Editor",
    page_icon="📸",
    layout="centered"
)


# Display the main application title.
st.title("📸 AI Photo Editor")

# Display a short description of the application.
st.write(
    "Upload an image and describe how you want to edit it using AI."
)


# Create a file uploader for JPG, JPEG, and PNG images.
uploaded_image = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)


# Continue only when the user uploads an image.
if uploaded_image:

    # Open the uploaded image using Pillow.
    image = Image.open(uploaded_image)

    # Display a heading for the original image.
    st.subheader("Original Image")

    # Display the uploaded image in the application.
    st.image(
        image,
        use_container_width=True
    )


    # Create a text box where the user can describe the desired edit.
    prompt = st.text_input(
        "Describe your edit",
        placeholder=(
            "Example: Remove the background and add a professional "
            "office background."
        )
    )


    # Create the button that starts the AI editing process.
    if st.button("✨ Generate Edited Image"):

        # Check whether the user has entered an editing instruction.
        if prompt:

            # Show a loading message while the AI processes the image.
            with st.spinner("AI is editing your image..."):

                # Send the uploaded image and user prompt to the AI editor.
                edited_image = edit_image(
                    image,
                    prompt
                )


            # Check whether the AI successfully returned an edited image.
            if edited_image:

                # Display a heading for the edited image.
                st.subheader("Edited Image")

                # Display the generated image.
                st.image(
                    edited_image,
                    use_container_width=True
                )


                # Create an in-memory buffer for the edited image.
                buffer = BytesIO()

                # Save the edited image into the buffer as PNG.
                edited_image.save(
                    buffer,
                    format="PNG"
                )


                # Create a download button for the edited image.
                st.download_button(
                    label="⬇️ Download Edited Image",
                    data=buffer.getvalue(),
                    file_name="edited_image.png",
                    mime="image/png"
                )


            # Show an error if the AI did not return an image.
            else:
                st.error(
                    "The AI could not generate an edited image."
                )


        # Show a warning if the user clicked the button without entering a prompt.
        else:
            st.warning(
                "Please enter an editing instruction."
            )