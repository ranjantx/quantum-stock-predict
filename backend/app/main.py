from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.quantum_stock_prediction import predict_quantum_stock

app = FastAPI(
    title="Quantum Stock Prediction API",
    description="Quantum + Classical ML Stock Forecast API (v0.4)",
    version="0.4"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # update this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Quantum Stock Prediction API v0.4"}

@app.get("/predict")
def run_prediction():
    result = predict_quantum_stock()
    return {"prediction": result}
