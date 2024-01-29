import pandas as pd
import os
from WaterQualityPredictor import logger
from sklearn.linear_model import ElasticNet
import joblib
from WaterQualityPredictor.entity.config_entity import ModelTrainerConfig
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.model_selection import GridSearchCV

class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config

    def train(self):
        
        train_data = pd.read_csv(self.config.train_data)
        test_data = pd.read_csv(self.config.test_data)
        logger.info(f'&&&&&&&&&&&&&&&&&:\nTrain data: {train_data}, Columns {train_data.columns}, Shape: {train_data.shape}')

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]

        # rdf = RandomForestClassifier(n_estimators=100, max_depth=20)

        parameters = {
            'n_estimators': [100, 200],
            'max_depth': [None, 10, 20, 30]
        }
        classifier=RandomForestClassifier()
        rdf = GridSearchCV(classifier,param_grid=parameters,cv=5)

        rdf.fit(train_x, train_y)

        joblib.dump(rdf, self.config.model_name)