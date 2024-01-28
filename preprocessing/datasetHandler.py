from utils.filterFolder import filter_folder_by_ext,filter_folder_by_name

import logging
import cv2
import rasterio
import glob

def xml_handler():
    logging.info("Handling images from GEE and SNAP ...")
    logging.info("Data originated from GEE and SNAP found ...")
    data = filter_folder_by_ext(".xml")
    data_sent2 = filter_folder_by_name()
    
   
    