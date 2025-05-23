from fastapi import FastAPI
from quantum_stock_prediction import predict_stock

app = FastAPI()

@app.get("/predict")
def predict():
    return predict_stock()
