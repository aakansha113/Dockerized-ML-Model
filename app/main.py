from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

app = FastAPI(title="ML Model API")

class InputData(BaseModel):
    features: list  # e.g. [5.1, 3.5, 1.4, 0.2]

# load model at startup
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def read_root():
    return {"message": "ML Model API running"}

@app.post("/predict")
def predict(payload: InputData):
    arr = np.array(payload.features).reshape(1, -1)
    pred = model.predict(arr)
    return {"prediction": int(pred[0])}

