import numpy as np
from service.luna_service import LunaService
from domain.exam import Exam


class LunaController:

    def __init__(self):
        self.exam = Exam()
        self.lunaService = LunaService()

    def predict(self, data) -> float | None:
        self.exam = Exam()

        self.exam.radius_mean = np.double(data.get("radius_mean"))
        self.exam.texture_mean = np.double(data.get("texture_mean"))
        self.exam.perimeter_mean = np.double(data.get("perimeter_mean"))
        self.exam.area_mean = np.double(data.get("area_mean"))
        self.exam.smoothness_mean = np.double(data.get("smoothness_mean"))
        self.exam.compactness_mean = np.double(data.get("compactness_mean"))
        self.exam.concavity_mean = np.double(data.get("concavity_mean"))
        self.exam.concave_points_mean = np.double(data.get("concave_points_mean"))
        self.exam.symmetry_mean = np.double(data.get("symmetry_mean"))
        self.exam.fractal_dimension_mean = np.double(data.get("fractal_dimension_mean"))
        self.exam.radius_se = np.double(data.get("radius_se"))
        self.exam.texture_se = np.double(data.get("texture_se"))
        self.exam.perimeter_se = np.double(data.get("perimeter_se"))
        self.exam.area_se = np.double(data.get("area_se"))
        self.exam.smoothness_se = np.double(data.get("smoothness_se"))
        self.exam.compactness_se = np.double(data.get("compactness_se"))
        self.exam.concavity_se = np.double(data.get("concavity_se"))
        self.exam.concave_points_se = np.double(data.get("concave_points_se"))
        self.exam.symmetry_se = np.double(data.get("symmetry_se"))
        self.exam.fractal_dimension_se = np.double(data.get("fractal_dimension_se"))
        self.exam.radius_worst = np.double(data.get("radius_worst"))
        self.exam.texture_worst = np.double(data.get("texture_worst"))
        self.exam.perimeter_worst = np.double(data.get("perimeter_worst"))
        self.exam.area_worst = np.double(data.get("area_worst"))
        self.exam.smoothness_worst = np.double(data.get("smoothness_worst"))
        self.exam.compactness_worst = np.double(data.get("compactness_worst"))
        self.exam.concavity_worst = np.double(data.get("concavity_worst"))
        self.exam.concave_points_worst = np.double(data.get("concave_points_worst"))
        self.exam.symmetry_worst = np.double(data.get("symmetry_worst"))
        self.exam.fractal_dimension_worst = np.double(data.get("fractal_dimension_worst"))

        return self.lunaService.predict(self.exam)

