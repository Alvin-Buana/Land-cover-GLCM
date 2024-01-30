from config.config import glcm_save_path

from skimage.feature import graycomatrix, graycoprops
from skimage.transform import resize
from scipy import ndimage
import pandas as pd
import numpy as np
import rasterio
import logging
import shutil
import tqdm
import cv2
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
#     df = pd.DataFrame(columns =["contrast","homogeneity","energy","entropy"])
#     distancess = [1, 2, 3, 4,5,6,7,8,9,10]  # Specify the distances to compute
#     angless = [0, np.pi/4, np.pi/2, 3*np.pi/4]  # Specify the angles to compute
#     for disc in tqdm(distancess,desc='Distance'):
#         for ang in tqdm(angless,desc='Angle'):
#             word = str(int(ang * 180 / np.pi))+"_"+str(disc)
#             df = pd.DataFrame(columns =["contrast_"+word,"homogeneity"+word,"energy"+word,"entropy"+word])
#             for item in tqdm(items,desc = 'Item'):
#               contrast,homogeneity,energy,entropy = perform_glcm(path+item,disc,ang)
#               df.loc[len(df)] =[contrast,homogeneity,energy,entropy]
#             df.to_csv(glcm_save_path +str(distances[0])+"_with_"+str(int(angles[0] * 180 / np.pi))+"_degree.csv")


def glcm(outRaster, sizeWindow):
    """
    Run the GLCM textures and append them into one 3D array
    The "ndimage.generic_filter" funtion perform the moving window of size "window"
    """
    # prepare textures
    def homogeneity_fun(outRaster):
        """
        create Homogeneity using the GLCM function 
        of Skimage
        """
        if len(outRaster.shape) == 1:
            outRaster = np.reshape(outRaster, (-1, sizeWindow))
            
        glcm = greycomatrix(outRaster, [1], [0], symmetric = True, normed = True)
        return greycoprops(glcm, 'homogeneity')[0,0]
        
    def correlation_fun(outRaster):
        """
        create Correlation using the GLCM function 
        of Skimage
        """
        if len(outRaster.shape) == 1:
            outRaster = np.reshape(outRaster, (-1, sizeWindow))
            
        glcm = greycomatrix(outRaster, [1], [0], symmetric = True, normed = True)
        return greycoprops(glcm, 'correlation')[0,0]
    
    def contrast_fun(outRaster):
        """
        create contrast using the GLCM function 
        of Skimage
        """
        if len(outRaster.shape) == 1:
            outRaster = np.reshape(outRaster, (-1, sizeWindow))
            
        glcm = greycomatrix(outRaster, [1], [0], symmetric = True, normed = True)
        return greycoprops(glcm, 'contrast')[0,0]
     
    def  dissimilarity_fun(outRaster):
        """
        create dissimilarity_fun using the GLCM function 
        of Skimage
        """
        if len(outRaster.shape) == 1:
            outRaster = np.reshape(outRaster, (-1, sizeWindow))
            
        glcm = greycomatrix(outRaster, [1], [0], symmetric = True, normed = True)
        return greycoprops(glcm, 'dissimilarity')[0,0]

    # apply to moving window
    Variance      = ndimage.generic_filter(outRaster, np.var, size=sizeWindow)
    Contrast      = ndimage.generic_filter(outRaster, contrast_fun, size=sizeWindow)
    Dissimilarity = ndimage.generic_filter(outRaster, dissimilarity_fun, size=sizeWindow)
    Correlation   = ndimage.generic_filter(outRaster, correlation_fun, size=sizeWindow)
    Homogeneity   = ndimage.generic_filter(outRaster, homogeneity_fun, size=sizeWindow)
    Entropy       = ndimage.generic_filter(outRaster, entropy, size=sizeWindow)
    
    return np.dstack( (Variance, Contrast, Dissimilarity, Correlation, Homogeneity, Entropy) )

def extract_raster(path):
    img = rasterio.open(path)
    raster = img.read()
    print(raster.shape)
    band = 3
    return raster[band-1,:,:]


    