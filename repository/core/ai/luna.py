import os
from tensorflow.keras.models import model_from_json


class Luna:
    __BASEPATH = f'{os.getcwd()}/repository/core/data'

    def __init__(self):
        with open(f'{Luna.__BASEPATH}/classifier_breast_json.json', 'r') as file:
            self.__model_structure_json = file.read()

        self.classifier = model_from_json(self.__model_structure_json)
        self.classifier.load_weights(f'{Luna.__BASEPATH}/weights_breast_for_classification.h5')
