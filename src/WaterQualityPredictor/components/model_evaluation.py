import pandas as pd
import os
from WaterQualityPredictor import logger
from sklearn.metrics import accuracy_score
from WaterQualityPredictor.constants import *
from WaterQualityPredictor.utils.common import save_json
from urllib.parse import urlparse
import joblib
import numpy as np
from pathlib import Path
from WaterQualityPredictor.entity.config_entity import ModelEvaluationConfig
import pickle

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        accuracy = accuracy_score(actual, pred)
        return accuracy

    def save_results(self):
        test_data = pd.read_csv(self.config.test_data)
        model = joblib.load(self.config.model)

        test_x = test_data.drop(self.config.target_column, axis=1)
        test_y = test_data[[self.config.target_column]]

        predicted = model.predict(test_x)

        accuracy = self.eval_metrics(test_y, predicted)

        # Saving the model as local
        scores = {"accuracy":accuracy}
        save_json(path=Path(self.config.metric_file_name), data=scores)