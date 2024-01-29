from WaterQualityPredictor import logger
from WaterQualityPredictor.entity.config_entity import DataValidationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
# from WaterQualityPredictor.utils.common import 
import os

from imblearn.over_sampling import SMOTE

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    logger.info(f'Data Validation failed at column: {col}')
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation status: {validation_status}')
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f'Validation status: {validation_status}')
            
            logger.info(f'schema: \n {all_schema}\n dataset columns: {all_cols}')
            return validation_status
        
        except Exception as e:
            raise e
        
    def split_data(self):
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            logger.info('Dataset read in the split_data method in the data validation class')

            ##########################################################
            # # Handling missing value as smote does not work with it
            # mean_cols = ['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
            # 'Organic_carbon', 'Trihalomethanes', 'Turbidity']  # Replace with your selected columns
            # data[mean_cols] = data[mean_cols].fillna(data[mean_cols].mean())

            # # Splitting our data
            # X = data.drop('Potability', axis=1)
            # y = data['Potability']

            # # Handling Imbalance using SMOTE to improve accuracy
            # smote = SMOTE(sampling_strategy='minority')
            # X, y = smote.fit_resample(X, y)

            # data = pd.concat([X, y], axis=1)
            ###########################################################

            train_set,test_set = train_test_split(data, test_size=0.15, random_state=2)
            logger.info(f'Train and test size: {train_set.shape,test_set.shape}')
            
            train_set.to_csv(self.config.train_data, index=False)
            logger.info(f'Train Data Saved')
            test_set.to_csv(self.config.test_data, index=False)
            logger.info(f'Test Data Saved')
        
        except Exception as e:
            raise e



        

            