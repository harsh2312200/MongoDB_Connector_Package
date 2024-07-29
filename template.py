import os
from pathlib import Path
import logging

package_name = "database_connection"

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


list_of_files = [
    ".github/workflows/ci.yaml",
    ".github/workflows/python-publish.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/integration.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiments.ipynb"]

for Filepath in list_of_files:
    filepath = Path(Filepath)
    file_dir,file_name = os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory : {file_dir} for file : {file_name}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath,"w") as f:
            pass # create empty file
        logging.info(f"Creating empty file: {filepath}")



