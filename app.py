import gradio as gr
from tensorflow.keras.models import load_model
from keras.preprocessing.image import img_to_array
from huggingface_hub import hf_hub_download
import numpy as np
from PIL import Image

# Load model from Hugging Face
model_path = hf_hub_download(
    repo_id="keshavsingh2003/brain-tumour-model",
    filename="model.h5",
    repo_type="model"
)
model = load_model(model_path)

# Class labels
class_labels = ['pituitary', 'glioma', 'notumor', 'meningioma']

# Prediction function
def predict_tumor(image):
    IMAGE_SIZE = 128
    img = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    confidence_score = np.max(predictions, axis=1)[0]

    if class_labels[predicted_class_index] == 'notumor':
        result = "🧠 No Tumor Detected"
    else:
        result = f"🧠 Tumor Detected: {class_labels[predicted_class_index].capitalize()}"

    return result, f"{confidence_score * 100:.2f}%"

# Gradio UI
interface = gr.Interface(
    fn=predict_tumor,
    inputs=gr.Image(type="pil", label="Upload MRI Image"),
    outputs=[
        gr.Textbox(label="Prediction"),
        gr.Textbox(label="Confidence Score")
    ],
    title="🧠 MRI Tumor Detection System",
    description="Upload an MRI image (JPG, JPEG, PNG) to detect if there is a tumor and what type it is."
)

interface.launch()
