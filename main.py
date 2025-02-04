from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys


if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the Data Ingestion process")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion process completed")
        print(dataingestionartifact)

        datavalidationconfig=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiated the Data Validation process")
        datavalidationartifact=data_validation.initiate_data_validation()
        logging.info("Data Validation process completed")
        print(datavalidationartifact)

        datatransformationconfig = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(datavalidationartifact, datatransformationconfig)
        logging.info("Initiated the Data Transformation process")
        datatransformationartifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation process completed")
        print(datatransformationartifact)

        logging.info("Initiated the Model Training process")
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config, 
                                     datatransformationartifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()

        logging.info("Model Training process completed")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)