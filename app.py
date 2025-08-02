import streamlit as st
from tensorflow.keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from huggingface_hub import hf_hub_download
import numpy as np
import os
from PIL import Image

# Title and intro
st.set_page_config(page_title="MRI Tumor Detection System", layout="centered")
st.title("🧠 MRI Tumor Detection System")
st.markdown("Upload an MRI image to detect if there is a tumor and its type.")

# Load model from Hugging Face
@st.cache_resource
def load_model_from_huggingface():
    model_path = hf_hub_download(
        repo_id="keshavsingh2003/brain-tumour-model",
        filename="model.h5",
        repo_type="model"
    )
    return load_model(model_path)

model = load_model_from_huggingface()

# Class labels
class_labels = ['pituitary', 'glioma', 'notumor', 'meningioma']

# Prediction Function
def predict_tumor(image):
    IMAGE_SIZE = 128
    img = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    confidence_score = np.max(predictions, axis=1)[0]

    if class_labels[predicted_class_index] == 'notumor':
        return "No Tumor", confidence_score
    else:
        return f"Tumor: {class_labels[predicted_class_index]}", confidence_score

# Upload File
uploaded_file = st.file_uploader("Choose an MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Detect Tumor"):
        with st.spinner("Analyzing Image..."):
            result, confidence = predict_tumor(image)
            st.success(f"**Result:** {result}")
            st.info(f"**Confidence:** {confidence * 100:.2f}%")
