import streamlit as st
from PIL import Image

st.subheader("Евгений, превращаю для тебя цветные фото в черно-белые с помощью Питона!!! "
             "Номер карты ты знаешь!")

uploaded_image = st.file_uploader("Тут можешь выбрать фото из своей библиотеки:")

with st.expander("Тут можешь включить камеру:"):
    # Start the camera
    camera_image = st.camera_input("Camera")


if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)


# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to grayscale
    gray_uploaded_img = img.convert('L')
    # Display the grayscale image on the webpage
    st.image(gray_uploaded_img)