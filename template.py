import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "WaterQualityPredictor"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath) # Converting the file path we specifyed in windows, we used backword slash but using the Path() class it converts it to windows path
    filedir, filename = os.path.split(filepath) # Split the filepath variable to the directory and file name
    
    if filedir != "": # If the file path contains a folder that means it is not a single file do the below
        os.makedirs(filedir, exist_ok=True) # Create the directory and if it exists no problem
        logging.info(f"Creating directory: {filedir} for the file: {filename}") # Log your progress

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # If the file exist or
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already existing")