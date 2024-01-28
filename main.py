from preprocessing.datasetHandler import xml_handler
from model.svm import modelSVC

# import numpy as np
import logging 
import os



if __name__ == '__main__':
    log_file = os.path.join(".", "logs")
    if not os.path.exists(log_file):
        os.mkdir(log_file)
    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s ",
    datefmt='%m/%d/%Y %I:%M:%S %p',
    handlers=[
        logging.FileHandler("./logs/basic.log"),

        logging.StreamHandler()
    ]
)
    
    
    logging.info('Program starting...')
    xml_handler()
