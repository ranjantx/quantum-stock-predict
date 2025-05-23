from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit.utils import algorithm_globals
from qiskit import BasicAer
#from qiskit.algorithms import QSVM
from qiskit_machine_learning.algorithms import QSVC
import numpy as np

def predict_stock():
    algorithm_globals.random_seed = 12345

    # Dummy training data
    X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_train = np.array([0, 1, 1, 0])

    feature_map = ZZFeatureMap(feature_dimension=2, reps=1)
    quantum_kernel = QuantumKernel(feature_map=feature_map, quantum_instance=BasicAer.get_backend("qasm_simulator"))

    model = QSVC(quantum_kernel=quantum_kernel)
    model.fit(X_train, y_train)

    # Predict
    test_sample = np.array([[0.5, 0.5]])
    prediction = model.predict(test_sample)

    return {"input": test_sample.tolist(), "predicted_class": int(prediction[0])}
