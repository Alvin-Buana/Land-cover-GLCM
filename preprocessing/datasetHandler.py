from utils.filterFolder import filter_folder_by_name
from utils.labelHandler import label_handler
from utils.glcm import glcm
from config.config import sent1_folder_name,sent2_folder_name,datadir

import logging
import cv2
import rasterio
import glob

def sent2_handler():
    data = glob.glob(datadir+'/*')
    data_sent2 = filter_folder_by_name(data, sent2_folder_name)
    

    
    
   
    