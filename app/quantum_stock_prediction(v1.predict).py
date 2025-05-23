
from pydantic import BaseModel
from qiskit_machine_learning.algorithms import VQR
import numpy as np
import joblib
import os

class StockInput(BaseModel):
    ticker: str
    days: int

class StockOutput(BaseModel):
    predicted_prices: list[float]

# Placeholder path to saved model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "vqr_model.joblib")

def predict_stock(input_data: StockInput) -> StockOutput:
    # Load model
    if not os.path.exists(MODEL_PATH):
        raise RuntimeError(f"Trained model not found at {MODEL_PATH}")

    model: VQR = joblib.load(MODEL_PATH)

    # Dummy encoding: turn 'ticker' + day index into numerical features
    features = np.array([[ord(c) % 10 for c in input_data.ticker][:2] + [i] for i in range(input_data.days)])

    # Pad features to expected size (depends on training config)
    features = np.array([np.pad(x, (0, max(0, model.feature_map.num_qubits - len(x))), constant_values=0)
                         for x in features])

    # Predict with model
    predictions = model.predict(features).tolist()

    return StockOutput(predicted_prices=predictions)
