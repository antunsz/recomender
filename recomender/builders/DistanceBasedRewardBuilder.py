from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd
from typing import Callable
import numpy as np
from recomender.interfaces import RewardBuilderAbstract

class DistanceBasedRewardBuilder(RewardBuilderAbstract):
    def __init__(self, dataframe: pd.DataFrame, distance_calculator: Callable[[np.ndarray, np.ndarray], float]):
        super().__init__(m=dataframe.shape[0], n=dataframe.shape[0])
        self.dataframe = dataframe
        self.distance_calculator = distance_calculator
        self.feature_matrix = self.preprocess_data()

    def preprocess_data(self) -> np.ndarray:
        categorical_features = self.dataframe.select_dtypes(include=['object', 'category']).columns.tolist()
        numerical_features = self.dataframe.select_dtypes(include=['float64', 'int64']).columns.tolist()

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_features),
                ('cat', OneHotEncoder(), categorical_features)
            ]
        )

        feature_matrix = preprocessor.fit_transform(self.dataframe)
        return feature_matrix

    def calculate_reward(self, row: int, column: int) -> float:
        vector_a = self.feature_matrix[row]
        vector_b = self.feature_matrix[column]
        distance = self.distance_calculator(vector_a, vector_b)
        return -distance
