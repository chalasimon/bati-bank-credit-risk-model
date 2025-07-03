from fastapi import FastAPI
from src.api.pydantic_models import InputData, PredictionResponse
import mlflow.sklearn
import pandas as pd

app = FastAPI(title="Credit Risk Model API")

# Load model from MLflow registry or local path
model = mlflow.sklearn.load_model("models:/RandomForest/Production")  # adjust name/version

@app.post("/predict", response_model=PredictionResponse)
def predict(input_data: InputData):
    features_df = pd.DataFrame([input_data.features])
    proba = model.predict_proba(features_df)[0][1]
    pred = model.predict(features_df)[0]
    return PredictionResponse(risk_probability=proba, predicted_class=int(pred))
