import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler


class Normalization:
    def __init__(self, X: np.ndarray) -> None:
        scaler = StandardScaler()
        self.scaler = scaler.fit(X)

    def transform(self, X: np.ndarray) -> np.ndarray:
        transformed_X = self.scaler.transform(X)

        return transformed_X

    def mean(self) -> np.ndarray:
        _mean = self.scaler.mean_

        return _mean

    def standard_deviation(self) -> np.ndarray:
        _variance = self.scaler.var_
        _standard_deviation = np.sqrt(_variance)

        return _standard_deviation


class MinMaxNormalization(Normalization):
    def __init__(self, X: np.ndarray) -> None:
        super().__init__()
        scaler = MinMaxScaler()
        self.scaler = scaler.fit(X)
