import numpy as np

from sklearn.svm import LinearSVC, SVC
from sklearn.pipeline import make_pipeline


class SVM:
    def __init__(self, _random_state: int = 0, _tol: float = 1e-5) -> None:
        self.model = SVC(random_state=_random_state, tol=_tol)
        self.classifier

    def build_pipeline(self, scaler) -> None:
        self.classifier = make_pipeline(scaler, self.model)

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        self.classifier.fit(X, y)

    def predict(self, X: np.ndarray) -> np.ndarray:
        predicted_y = self.classifier.predict(X)

        return predicted_y


class LinearSVM(SVM):
    def __init__(self, _random_state: int = 0, _tol: float = 1e-5) -> None:
        super().__init__(_random_state, _tol)
        self.model = LinearSVC(random_state=_random_state, tol=_tol)
