import numpy as np
from repository.luna_repository import LunaRepository
from domain.exam import Exam


class LunaService:
    def __init__(self):
        self.lunaRepository = LunaRepository()

    def predict(self, exam: Exam) -> float | None:
        prediction = self.lunaRepository.predict(exam)
        if not np.isnan(prediction):
            return prediction

        return None
