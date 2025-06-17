# Question Pair Duplicate Detection API
This is a FastAPI-based REST API that classifies whether two questions are duplicates using a fine-tuned BERT model. The model is stored externally on Google Drive and automatically downloaded when the app starts.

## Features
- FastAPI + Pydantic
- BERT-based model for question similarity
- Automatic model download from Google Drive
- Docker-ready structure
- JSON input/output for easy integration

## 📦 Installation
```sh
git clone https://github.com/nvkoval/ml_api.git
cd ml_api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn app:app --reload
```

## 🐳 Run with Docker
```sh
docker build -t ml-api .
docker run -d -p 8000:8000 ml-api
```
On first run, the model will be downloaded from Google Drive into the `models/` folder.

## API Endpoints
`POST /predict/`
Check if two questions are duplicates.

**Request JSON**
```json
{
  "question1": "Why is beef banned in India and not pork as well?",
  "question2": "Is beef banned in india?"
}
```

**Response JSON**
```json
{
  "class_name": true,
  "confidence": 0.91
}
```

**`GET /`**

Welcome message.
```json
{
  "message": "Welcome to the ML API! Use the /predict endpoint to classify question pairs."
}
```

## 📁 Project Structure
```
ml-api/
├──app/
| ├── main.py            # FastAPI app
| ├── model.py           # Model loading and prediction logic
| ├── schemas.py         # Pydantic models
| └── utils.py           # Model download utility
├──models/               # Will contain downloaded model (ignored in Git)
├──requirements.txt
├──Dockerfile (optional)
├──README.md
```

## Model Details
- Architecture: `BertForSequenceClassification`
- Trained on: Quora Question Pairs dataset
- Exported using: `transformers model.save_pretrained()`

## Model Download
- To keep the repository lightweight, the transformer model is stored externally on Google Drive.
- During first run, the model folder will be automatically downloaded to `models/transformer_model/` using the public folder link.

## 📌 Notes
- Make sure you have internet access on first run (for downloading the model).
- Add your own model by updating the `FOLDER_ID` in `app/model.py`.
