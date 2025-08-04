
<img width="1439" height="803" alt="Screenshot 2025-08-04 at 10 39 30 PM" src="https://github.com/user-attachments/assets/1b65785f-e9cc-4c63-8e64-d980b6bd0da9" />





# 🧠 Handwritten Digit Classifier

A web-based digit recognition app that classifies handwritten digits using a deep learning model trained on the MNIST dataset.

This project is built using **Streamlit** for the web interface and **TensorFlow** for the machine learning backend.

---

## 🔍 Features

- Upload a digit image (28x28 grayscale) or provide an image path  
- Real-time digit prediction  
- Displays prediction confidence  
- Easy-to-use and intuitive UI  
- Built with 💖 using Streamlit and TensorFlow  

---

## 🧪 Model

The model is trained on the https://github.com/Muahammad-Umair/Digit-prediction-system-with-streamlit-ui), which consists of 60,000 training images and 10,000 testing images of handwritten digits (0 through 9).

---

## 🛠️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Muahammad-Umair/Digit-prediction-system-with-streamlit-ui
cd handwritten-digit-classifier

## Project Structure

├── prediction.py            # Main Streamlit app file
├── class.ipynb              # Model training or utility notebook
├── model/                   # (Optional) Saved Keras/TensorFlow model
├── images/                  # Example digit images
├── README.md                # Documentation

✅ Example Output
Uploaded image of handwritten digit "3"

✅ Predicted Digit: 3

📊 Confidence: 100.00%

