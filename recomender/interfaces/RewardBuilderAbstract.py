from abc import ABC, abstractmethod
import numpy as np
from typing import Protocol

class DistanceCalculator(Protocol):
    def __call__(self, vector_a: np.ndarray, vector_b: np.ndarray) -> float:
        pass

class RewardBuilderAbstract(ABC):
    def __init__(self, m: int, n: int):
        """
        Initialize the RewardBuilder with dimensions for the reward matrix.
        
        Parameters:
            m (int): The number of rows in the matrix.
            n (int): The number of columns in the matrix.
        """
        self.m = m
        self.n = n

    @abstractmethod
    def calculate_reward(self, row: int, column: int) -> float:
        """
        Calculate the reward for a given pair of entities.

        Parameters:
            row (int): Represents one entity (e.g., an action or an item).
            column (int): Represents another entity (e.g., a state or another item).

        Returns:
            float: The calculated reward for the given entities.
        """
        pass

    def build_reward_matrix(self) -> np.ndarray:
        """
        Generates an m x n reward matrix based on the interactions between entities represented by rows and columns.

        Returns:
            np.ndarray: An m x n matrix of rewards.
        """
        reward_matrix = np.zeros((self.m, self.n))
        for i in range(self.m):
            for j in range(self.n):
                reward_matrix[i, j] = self.calculate_reward(i, j)
        return reward_matrix
