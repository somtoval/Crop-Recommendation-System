from WaterQualityPredictor.entity.config_entity import DataTransformationConfig
import pandas as pd
from WaterQualityPredictor import logger
from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

from imblearn.over_sampling import SMOTE

import os 
import pickle
import numpy as np

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def get_preprocessor(self):
        try:
            # logger.info('Data Transformation')
            # # Feature Scaling
            # steps = [("standard_scaler", StandardScaler())]

            # preprocessor = Pipeline(steps)

            train_set = pd.read_csv(self.config.train_data)
            test_set = pd.read_csv(self.config.test_data)

            logger.info('Data Transformation')
            # Feature Scaling and Feature Encoding
            num_steps = [("standard_scaler", StandardScaler())]

            numeric_pipe = Pipeline(steps=num_steps)

            numeric_features = train_set.select_dtypes(include=['float64', 'int64']).columns[:-1]

            preprocessor = ColumnTransformer(transformers=[
                    ('num', numeric_pipe, numeric_features),
            ],remainder='passthrough')
            
            with open(self.config.preprocessor_obj, "wb") as file_obj:
                pickle.dump(preprocessor, file_obj)
                logger.info(f'Preprocessor Object saved')

        except Exception as e:
            logger.info('Error in Data Transformation', e)

        return preprocessor

    def data_transformation(self, train_set, test_set):
        train_set = pd.read_csv(train_set)
        test_set = pd.read_csv(test_set)

        numeric_features = train_set.columns
        logger.info(f'Numeric columns:\n {numeric_features}')

        # Handling Missing Values
        # Replace missing values with the mean of selected columns
        mean_cols = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
            'Organic_carbon', 'Trihalomethanes', 'Turbidity']  # Replace with your selected columns
        train_set[mean_cols] = train_set[mean_cols].fillna(train_set[mean_cols].mean())
        test_set[mean_cols] = test_set[mean_cols].fillna(test_set[mean_cols].mean())
        # # Replace missing values with the median of selected columns
        # median_cols = ['Solids']  # Replace with your selected columns
        # train_set[median_cols] = train_set[median_cols].fillna(train_set[median_cols].median())
        # test_set[median_cols] = test_set[median_cols].fillna(test_set[median_cols].median())

        # Handling Imbalance
        # Splitting our train data
        X = train_set.drop('Potability', axis=1)
        y = train_set['Potability']

        # Handling Imbalance using SMOTE to improve accuracy
        # smote = SMOTE(sampling_strategy='minority')
        # X, y = smote.fit_resample(X, y)

        # train_set = pd.concat([X, y], axis=1)

        ################################
        # # Splitting our data
        # Xt = test_set.drop('Potability', axis=1)
        # yt = test_set['Potability']

        # # Handling Imbalance using SMOTE to improve accuracy
        # smote = SMOTE(sampling_strategy='minority')
        # Xt, yt = smote.fit_resample(Xt, yt)

        # test_set = pd.concat([Xt, yt], axis=1)
        ################################

        preprocessor = self.get_preprocessor()

        train_set = preprocessor.fit_transform(train_set)
        test_set = preprocessor.transform(test_set)
        
        transformed_feature_names = numeric_features.tolist()

        # Convert the transformed array back to a DataFrame with meaningful column names
        train_set = pd.DataFrame(train_set, columns=transformed_feature_names)
        test_set = pd.DataFrame(test_set, columns=transformed_feature_names)

        logger.info(f'These are the columns:\n {train_set.columns} \n{test_set.columns}')

        train_set.to_csv(self.config.trf_train_data, index=False)
        logger.info(f'Preprocessed train data saved')

        test_set.to_csv(self.config.trf_test_data, index=False)
        logger.info(f'Preprocessed test data saved')