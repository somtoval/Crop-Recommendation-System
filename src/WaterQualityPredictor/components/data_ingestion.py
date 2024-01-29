import os
import urllib.request as request
import zipfile
from WaterQualityPredictor import logger
from WaterQualityPredictor.utils.common import get_size
from WaterQualityPredictor.entity.config_entity import DataIngestionConfig
from pathlib import Path
import shutil

class DataIngestion:
    def __init__(self, config:DataIngestionConfig) -> None:
        self.config = config

    def getfile(self):
        if not os.path.exists(self.config.local_data_file):
            shutil.copy(self.config.source_URL, self.config.local_data_file)
            logger.info(f"{os.path.basename(self.config.local_data_file)}")
        else:
            logger.info(f'File already exists, FILE SIZE:{get_size(Path(self.config.local_data_file))}')

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
        