from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

# Load model
model_path = "models/insurance_model.pkl"
model = joblib.load(model_path)  # model.dump() is typically used for Pydantic models, joblib.load still needed for sklearn

# Initialize FastAPI
app = FastAPI(title="Insurance Charges Prediction API")

# Define input schema
class InputData(BaseModel):
    age: float
    bmi: float
    children: float
    sex_female: float
    sex_male: float
    smoker_no: float
    smoker_yes: float
    region_northeast: float
    region_northwest: float
    region_southeast: float
    region_southwest: float

# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.model_dump()])  # convert input to DataFrame
    prediction = model.predict(df)
    return {"predicted_charges": float(prediction[0])}

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Insurance Charges Prediction API"}
