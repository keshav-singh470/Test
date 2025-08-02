from huggingface_hub import hf_hub_download
from tensorflow.keras.models import load_model

def load_model_from_hf():
    model_path = hf_hub_download(
        repo_id="keshavsingh2003/brain-tumour-model",
        filename="model.h5",
        repo_type="model"
    )
    return load_model(model_path)
