from WaterQualityPredictor.config.configuration import ConfigurationManager
from WaterQualityPredictor.components.model_evaluation import ModelEvaluation
from WaterQualityPredictor import logger
from pathlib import Path

STAGE_NAME = 'Model Evaluation stage'

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<\n\nx========================x")
    except Exception as e:
        logger.exception(e)
        raise e