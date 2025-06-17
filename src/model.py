import torch
from transformers import BertTokenizer, BertForSequenceClassification

from src.utils import load_model_if_needed

BASE_DIR = "models/"
MODEL_DIR = "models/bert_quora_model/"
FOLDER_ID = "1IohIVIrM9S9O2z2ljnDCYuFHPdVn0OTm"

load_model_if_needed(BASE_DIR, FOLDER_ID)

tokenizer = BertTokenizer.from_pretrained(MODEL_DIR)
model = BertForSequenceClassification.from_pretrained(MODEL_DIR)
model.eval()


def predict(question1: str,
            question2: str) -> tuple[bool, float]:
    encoding = tokenizer(
        question1,
        question2,
        truncation=True,
        padding=True,
        max_length=256,
        return_tensors=None
    )

    input_ids = torch.unsqueeze(
        torch.tensor(encoding['input_ids']), dim=0
    ).cpu()
    attention_mask = torch.unsqueeze(
        torch.tensor(encoding['attention_mask']), dim=0
    ).cpu()

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)

    probability = predictions[0][1].item()
    is_duplicate = probability > 0.5
    confidence = round(max(probability, 1 - probability), 4)
    if is_duplicate:
        is_duplicate = "duplicate"
    else:
        is_duplicate = "not duplicate"

    return is_duplicate, confidence
