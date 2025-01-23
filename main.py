from src.datascience import logger
from src.datascience.pipeline.Data_ingestion_pipeline import  DataIngestionTrainingPipeline
from src.datascience.pipeline.Data_Validation_pipeline import DataValidationPipeline
from src.datascience.pipeline.Data_transformation_pipeline import DataTransformationPipeline
from src.datascience.pipeline.Model_training_pipeline import ModelTrainingPipeline
from src.datascience.pipeline.Model_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f'>>>>>> stage: {STAGE_NAME} completed<<<<<<<\n\nx=====================================x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.initiate_data_validation()
    logger.info(f'>>>>>> stage: {STAGE_NAME} completed<<<<<\n\nx====================================x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f'>>>>>> stage: {STAGE_NAME} completed<<<<<\n\nx====================================x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.initiate_model_training()
    logger.info(f'>>>>>> stage: {STAGE_NAME} completed<<<<<\n\nx====================================x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_eval = ModelEvaluationPipeline()
    model_eval.initiate_model_Evaluation()
    logger.info(f'>>>>>> stage: {STAGE_NAME} completed<<<<<\n\nx====================================x')
except Exception as e:
    logger.exception(e)
    raise e
