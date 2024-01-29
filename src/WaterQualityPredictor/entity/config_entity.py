from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)# When you set frozen=True, it means that instances of the data class are considered immutable, meaning their attributes cannot be modified after they are created. This can be useful for creating objects that should not change once they are instantiated, ensuring their integrity and preventing unintended modifications.
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict
    train_data: Path
    test_data: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    train_data: Path
    test_data: Path
    trf_train_data: Path
    trf_test_data: Path
    preprocessor_obj: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    model_name: str
    target_column: str
    preprocessor_obj: Path
    train_data: Path
    test_data: Path
    fitted_preprocessor_obj: Path

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data: Path
    model: Path
    metric_file_name: Path
    target_column:str
    preprocessor_obj: Path