import os

from fastapi import FastAPI

from .predict import AutoLGBMPredict


app = FastAPI()
axgp = AutoLGBMPredict(model_path=os.environ.get("AUTOLGBM_MODEL_PATH"))
schema = axgp.get_prediction_schema()


@app.post("/predict")
def predict(sample: schema):
    sample = sample.json()
    return axgp.predict_single(sample)
