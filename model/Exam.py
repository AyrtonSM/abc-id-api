class Exam:

    def __init__(self):
    
        self.radius_mean = ''
        self.texture_mean = ''
        self.perimeter_mean = ''
        self.area_mean = ''
        self.smoothness_mean = ''
        self.compactness_mean = ''
        self.concavity_mean = ''
        self.concave_points_mean = ''
        self.symmetry_mean = ''
        self.fractal_dimension_mean = ''
        self.radius_se = ''
        self.texture_se = ''
        self.perimeter_se = ''
        self.area_se = ''
        self.smoothness_se = ''
        self.compactness_se = ''
        self.concavity_se = ''
        self.concave_points_se = ''
        self.symmetry_se = ''
        self.fractal_dimension_se = ''
        self.radius_worst = ''
        self.texture_worst = ''
        self.perimeter_worst = ''
        self.area_worst = ''
        self.smoothness_worst = ''
        self.compactness_worst = ''
        self.concavity_worst = ''
        self.concave_points_worst = ''
        self.symmetry_worst = ''
        self.fractal_dimension_worst = ''
        
    def to_list(self):
        return [[
            self.radius_mean,
            self.texture_mean,
            self.perimeter_mean,
            self.area_mean,
            self.smoothness_mean,
            self.compactness_mean,
            self.concavity_mean,
            self.concave_points_mean,
            self.symmetry_mean,
            self.fractal_dimension_mean,
            self.radius_se,
            self.texture_se,
            self.perimeter_se,
            self.area_se,
            self.smoothness_se,
            self.compactness_se,
            self.concavity_se,
            self.concave_points_se,
            self.symmetry_se,
            self.fractal_dimension_se,
            self.radius_worst,
            self.texture_worst,
            self.perimeter_worst,
            self.area_worst,
            self.smoothness_worst,
            self.compactness_worst,
            self.concavity_worst,
            self.concave_points_worst,
            self.symmetry_worst,
            self.fractal_dimension_worst
        ]]