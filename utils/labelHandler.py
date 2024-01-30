from utils.filterFolder import filter_folder_by_ext,filter_folder_by_name
from config.config import sent1_folder_name,sent2_folder_name

import logging


def label_handler():
    logging.info("Handling images from GEE and SNAP ...")
    logging.info("Data originated from GEE and SNAP found ...")
    labels_xml = filter_folder_by_ext(".xml")
    labels_txt = filter_folder_by_ext(".txt")
    return data