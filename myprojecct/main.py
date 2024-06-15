from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>> stage {STAGE_NAME} started <<<")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f">>> stage {STAGE_NAME} completed <<< \n")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME="Prepare Base Model"

try:
        logger.info(f">>> stage {STAGE_NAME} started <<<")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>> stage {STAGE_NAME} completed <<< \n")
except Exception as e:
        logger.exception(e)
        raise e
