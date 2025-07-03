from pydantic import BaseModel
from typing import List, Dict, Any
class InputData(BaseModel):
    features: Dict[str, Any] 
class PredictionResponse(BaseModel):
    risk_probability: float
    predicted_class: int
