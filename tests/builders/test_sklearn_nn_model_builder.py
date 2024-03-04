import numpy as np
import pytest
from sklearn.datasets import make_classification
from recomender.builders.SklearnNNModelBuilder import SklearnNNModelBuilder

@pytest.fixture
def synthetic_classification_data():
    """Generate a synthetic dataset for testing."""
    X, y = make_classification(n_samples=100, n_features=20, n_informative=15, n_redundant=5, random_state=42)
    return X, y

def test_sklearn_nn_model_builder_build():
    """Test that SklearnNNModelBuilder builds an instance of SklearnNNModel."""
    builder = SklearnNNModelBuilder()
    model = builder.build()
    assert model is not None, "Failed to build a model instance"

def test_sklearn_nn_model_training_and_prediction(synthetic_classification_data):
    """Test that the SklearnNNModel can be trained and make predictions."""
    X, y = synthetic_classification_data
    builder = SklearnNNModelBuilder()
    model = builder.build()

    # Splitting the synthetic data for training and testing
    X_train, X_test = X[:80], X[80:]
    y_train, y_test = y[:80], y[80:]

    # Training the model
    model.train(X_train, y_train)

    # Making predictions
    predictions = model.predict(X_test)
    assert len(predictions) == len(y_test), "The number of predictions does not match the number of test samples"
    assert (predictions == y_test).any(), "The model did not learn to classify the synthetic data correctly"


