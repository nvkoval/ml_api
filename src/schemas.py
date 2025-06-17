from pydantic import BaseModel


class PredictionRequest(BaseModel):
    question1: str
    question2: str

    class Config:
        json_schema_extra = {
            "example": {
                "question1": "Why is beef banned in India and not pork as well?",
                "question2": "Is beef banned in india?"
            }
        }


class PredictResponse(BaseModel):
    class_name: str
    confidence: float

    class Config:
        json_schema_extra = {
            "example": {
                "class_name": "not duplicate",
                "confidence": 0.9058
            }
        }
