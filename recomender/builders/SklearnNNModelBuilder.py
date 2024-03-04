from sklearn.neural_network import MLPClassifier
from recomender.interfaces import SLModelBuilderAbstract, Model
import numpy as np

class SklearnNNModel(Model):
    def __init__(self, model):
        self.model = model
    
    def train(self, X: np.ndarray, y: np.ndarray, **kwargs):
        self.model.fit(X, y)
    
    def predict(self, X: np.ndarray, **kwargs) -> np.ndarray:
        return self.model.predict(X)

class SklearnNNModelBuilder(SLModelBuilderAbstract):
    def build(self) -> Model:
        # Initialize the MLPClassifier with a simple architecture and configuration
        # This configuration can be customized as needed
        mlp_model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, activation='relu', solver='adam', random_state=1)
        
        # Wrap and return the MLPClassifier in a Model-compliant object
        return SklearnNNModel(mlp_model)

