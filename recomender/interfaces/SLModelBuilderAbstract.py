from abc import ABC, abstractmethod
import numpy as np
from typing import Any, Protocol

class Model(Protocol):
    def train(self, X: np.ndarray, y: np.ndarray, **kwargs) -> Any:
        """
        Train the model on the given dataset.

        Parameters:
            X (np.ndarray): The input features for training.
            y (np.ndarray): The target outputs for training.
            kwargs: Additional keyword arguments for training configurations.

        Returns:
            Any: The outcome of the training process, which could vary between implementations.
        """
        pass

    def predict(self, X: np.ndarray, **kwargs) -> np.ndarray:
        """
        Make predictions with the trained model.

        Parameters:
            X (np.ndarray): The input features for prediction.
            kwargs: Additional keyword arguments for prediction configurations.

        Returns:
            np.ndarray: The predicted outputs.
        """
        pass

class SLModelBuilderAbstract(ABC):
    @abstractmethod
    def build(self) -> Model:
        """
        Constructs and returns a model instance.

        Returns:
            Model: An instance of a model adhering to the Model protocol.
        """
        pass
