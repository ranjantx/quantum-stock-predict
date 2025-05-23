from fastapi import FastAPI
from pydantic import BaseModel
from quantum_stock_prediction import predict_stock

app = FastAPI()

# Define request model
class StockInput(BaseModel):
    ticker: str
    days: int

# Define response model (optional)
class StockOutput(BaseModel):
    predicted_prices: list[float]

@app.post("/predict", response_model=StockOutput)
def predict(input: StockInput):
    return predict_stock(input)
