# Data Handler
from utils.filterFolder import filter_folder_by_name
from utils.labelHandler import label_handler
from utils.glcm import perform_glcm
from utils.check_folder import checkFolder

#GLCM
from utils.glcm import extract_raster,perform_glcm,perform_single_glcm

#Config
from config.config import sent1_folder_name,sent2_folder_name,datadir,img_size,glcm_save_path,glcm_method,distances,angles

#Enviroment Libraries
import pandas as pd
import numpy as np
import logging
import cv2
import rasterio
import glob
import os

def sent2_handler():
    data = glob.glob(datadir+'\*')
    data_sent2 = filter_folder_by_name(data, sent2_folder_name)
    logging.info(data_sent2)

    checkFolder(glcm_save_path)
   
    for key in range(len(data_sent2)):
        logging.info(f"Performing GLCM on path {data_sent2[key]}")
        images = glob.glob(data_sent2[key]+'\images\*.tif')
        logging.info(f"Detected {len(images)} on {data_sent2[key]}")
        folder_name = data_sent2[key].split('\\')[1].split(sent2_folder_name)[0]
        if glcm_method == 1:
            for img in images:
                csv_name = img.split('\\')[-1].split('.tif')[0]
                saved_path = glcm_save_path+"/"+folder_name+"_"+csv_name+".csv"
                if not os.path.exists(saved_path):
                    raster = extract_raster(img,img_size,3)
                    glcm = perform_glcm(raster,7)
                    glcm = glcm.reshape(len(glcm),-1)
                    X = pd.DataFrame(glcm)
                    X.fillna(0,inplace=True)
                    X['label'] = key+1
                    saved_path = glcm_save_path+"/"+folder_name+"_"+csv_name+".csv"
                    X.to_csv(saved_path)
                    

                    logging.info(f"Saved path at {saved_path}")
                else:
                    logging.info(f"Path {saved_path} has been created previously ...")
        elif glcm_method == 2:
                distancess = distances
                angless = angles
                for distance in distancess:
                    for angle in angless:
                        word = str(int(angle * 180 / np.pi))+"_"+str(distance)
                        df = pd.DataFrame(columns =["contrast_"+word,"dissimilarity_"+word,"homogeneity_"+word,"energy_"+word,"entropy_"+word])
                        saved_path = glcm_save_path+"/"+folder_name+"_"+word+".csv"
                        if not os.path.exists(saved_path):
                            for img in images:
                                raster = extract_raster(img,img_size,3)
                                name =img.split('\\')[-1]
                                logging.info(f"Processing GLCM on {name}")
                                glcm = perform_single_glcm(raster,distance,angle)
                                df.loc[len(df)] = glcm
                            df['label'] = key+1    
                            df.to_csv(saved_path)
                            logging.info(f"Saved path at {saved_path}")
                        else:
                            logging.info(f"Path {saved_path} has been created previously ...")
                            

        else:
            raise ValueError('GLCM method did not follow the config. Please check your config')

    

    
    
   
    