import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import io

# Load the trained model
model = tf.keras.models.load_model('mnist_model.h5')  # Update with your model path

st.set_page_config(page_title="Digit Predictor", page_icon="🔢", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🧠 Handwritten Digit Classifier</h1>
    <p style='text-align: center;'>Upload a digit image or provide a path to predict</p>
""", unsafe_allow_html=True)

# --- Sidebar for input ---
st.sidebar.header("Upload or Path")
upload_method = st.sidebar.radio("Choose input method", ["Upload Image", "Enter Image Path"])

image = None

if upload_method == "Upload Image":
    uploaded_file = st.sidebar.file_uploader("Upload an image (28x28 grayscale)", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert('L')
else:
    path = st.sidebar.text_input("Enter image path (e.g., '3_digit.png')")
    if path:
        try:
            image = Image.open(path).convert('L')
        except FileNotFoundError:
            st.sidebar.error("File not found. Please check the path.")

# --- Main Area ---
if image:
    st.image(image, caption="Uploaded Image", width=150)

    # Preprocess
    img_resized = image.resize((28, 28))
    img_array = np.array(img_resized).reshape(1, 28, 28, 1).astype("float32") / 255.0

    # Prediction
    if st.button("🔍 Predict"):
        prediction_val = model.predict(img_array)
        predicted_digit = np.argmax(prediction_val).item()
        confidence = np.max(prediction_val) * 100

        st.success(f"🎯 Predicted Digit: **{predicted_digit}**")
        st.info(f"Confidence: {confidence:.2f}%")
else:
    st.warning("Please upload an image or provide a valid path.")

# Footer
st.markdown("""
<hr>
<p style='text-align: center; font-size: 13px;'>Built with ❤️ using Streamlit & TensorFlow</p>
""", unsafe_allow_html=True)
