from preprocessing.datasetHandler import sent2_handler
from config.config import img_size
from prepareModel.prepareAndTraining import sent2_data_prep

import matplotlib.pyplot as plt
from rasterio.plot import show
import numpy as np
import rasterio
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
    sent2_handler()
    sent2_data_prep()
    #For testing
    # tester = '.\data\hutan (Sent-2)\images\\000000000.tif'
    # tester = extract_raster(tester,img_size,3)
    # res=perform_single_glcm(tester,1,0)
    # print(res)
    logging.info('DONE')
    


    
