from huggingface_hub import HfApi
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get token from environment
hf_token = os.getenv("HF_TOKEN")

# Authenticate with token
api = HfApi(token=hf_token)

# Upload file
api.upload_file(
    path_or_fileobj="Models/model.h5",
    path_in_repo="model.h5",
    repo_id="keshavsingh2003/brain-tumour-model",
    repo_type="model"
)
