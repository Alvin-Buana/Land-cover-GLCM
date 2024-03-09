from config.config import glcm_save_path
from utils.glcm import perform_single_glcm

import pandas as pd
import logging
import tqdm
import os


def path_glcm(path):
    if os.path.exists(glcm_save_path):
        shutil.rmtree(glcm_save_path)
    os.mkdir(glcm_save_path)
    logging.info(f"Doing GLCM on {path} ...")

    
#     if not os.listdir(path):
#         raise exception("Path is having an error")
    items = os.listdir(path)
    items.sort()
    df = pd.DataFrame(columns =["contrast","homogeneity","energy","entropy"])
    distancess = [1, 2, 3, 4,5,6,7,8,9,10]  # Specify the distances to compute
    angless = [0, np.pi/4, np.pi/2, 3*np.pi/4]  # Specify the angles to compute
    for disc in tqdm(distancess,desc='Distance'):
        for ang in tqdm(angless,desc='Angle'):
            word = str(int(ang * 180 / np.pi))+"_"+str(disc)
            df = pd.DataFrame(columns =["contrast_"+word,"homogeneity"+word,"energy"+word,"entropy"+word])
            for item in tqdm(items,desc = 'Item'):
              contrast,homogeneity,energy,entropy = perform_single_glcm(path+item,disc,ang)
              df.loc[len(df)] =[contrast,homogeneity,energy,entropy]
    df.to_csv(glcm_save_path +str(distances[0])+"_with_"+str(int(angles[0] * 180 / np.pi))+"_degree.csv")
