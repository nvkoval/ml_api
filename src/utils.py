import os
import gdown


def load_model_if_needed(model_dir: str,
                         folder_id: str):
    if not os.path.exists(model_dir):
        os.makedirs(model_dir, exist_ok=True)
        print("Downloading model from Google Drive...")
        gdown.download_folder(
                id=folder_id,
                output=model_dir,
                quiet=False,
                use_cookies=False
            )
