#code of all common utility

import yaml
import os
import yaml
import logging
import time
import pandas as pd
import json
from zipfile import ZipFile

def read_yaml(path_to_yaml: str) ->dict:
    '''
    :arg string object
    :param path_to_yaml: will be a string
    :return: a dictionary of params values
    '''
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_loads(yaml_file)
    logging.info(f"yaml file {path_to_yaml} loaded successfully")
    return content
def create_directories(path_to_directories: list)->None:
    '''
    function tocreate directories for given path if not exist
    :param path_to_directories: dictinary values
    :return: none
    '''

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"created directories at : {path}")
def save_json(path: str, data: dict) -> None:
    ''':arg path as string and data as dictinary
    '''
    with open(path, "w") as f:
        json.dump(data,f, indent=4)
    logging.info(f"json file saved at :{path}")

def unzip_file(source: str, dest: str) -> None:
    ''':args
    source as string and destination as string type
    '''
    logging.info(f"extraction started...")

    with ZipFile(source, "r") as zip_f:
        zip_f.extractall(dest)
    logging.info(f"extracted {source} to {dest}")


