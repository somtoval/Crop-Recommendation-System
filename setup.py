from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def required_installs(requirement_path:str)-> List[str]:
    requirements = []
    with open(requirement_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Water-Quality-Predictor"
AUTHOR_USER_NAME = "Somto Ogbe"
SRC_REPO = "WaterQualityPredictor"
AUTHOR_EMAIL = "ogbesomto4@gmail.com"


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Water Quality Predictor Machine Learning Project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)