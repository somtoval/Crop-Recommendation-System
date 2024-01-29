from WaterQualityPredictor.config.configuration import ConfigurationManager
from WaterQualityPredictor.components.data_transformation import DataTransformation
from WaterQualityPredictor import logger

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.get_preprocessor()
        train_set = data_transformation_config.train_data
        test_set = data_transformation_config.test_data
        data_transformation.data_transformation(train_set, test_set)

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========================x")
    except Exception as e:
        logger.exception(e)
        raise e