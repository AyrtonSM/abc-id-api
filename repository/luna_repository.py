import numpy as np
from domain.exam import Exam



class LunaRepository:
    def __init__(self):
        pass

    def predict(self, exam: Exam) -> float:
        from app import luna
        if exam is not None:
            return luna.classifier.predict(np.array(exam.to_list()))[0][0]

        return np.nan
