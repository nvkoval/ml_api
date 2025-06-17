from fastapi import FastAPI
from src.schemas import PredictionRequest, PredictResponse
from src.model import predict

app = FastAPI(
    title="Question Pairs Duplicate Classification API",
    description="API for classifying question pairs using BERT"
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the ML API!"
            "Use the /predict endpoint to classify question pairs."}


@app.post("/predict/", response_model=PredictResponse)
def predict_duplicate(request: PredictionRequest):
    is_duplicate, confidence = predict(request.question1,
                                       request.question2)

    return PredictResponse(class_name=is_duplicate,
                           confidence=confidence)
