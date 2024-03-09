

from skimage.feature import graycomatrix, graycoprops
from skimage.transform import resize
from skimage.measure import shannon_entropy
from scipy.stats import entropy
from scipy import ndimage
import pandas as pd
import numpy as np
import rasterio
import logging
import shutil
import tqdm
import cv2
import os



 # prepare textures

def perform_glcm(outRaster, sizeWindow=7):
    """
    Run the GLCM textures and append them into one 3D array
    The "ndimage.generic_filter" funtion perform the moving window of size "window"
    """
    def homogeneity_fun(outRaster):
        """
        create Homogeneity using the GLCM function 
        of Skimage
        """
        if len(outRaster.shape) == 1:
            outRaster = np.reshape(outRaster, (-1, sizeWindow)).astype('uint8')
            
        glcm = graycomatrix(outRaster, [1], [0], symmetric = True, normed = True)
        return graycoprops(glcm, 'homogeneity')[0,0]
        
    def correlation_fun(outRaster):
        """
        create Correlation using the GLCM function 
        of Skimage
        """
        if len(outRaster.shape)== 1:
            outRaster = np.reshape(outRaster, (-1, sizeWindow)).astype('uint8')
            
        glcm = graycomatrix(outRaster, [1], [0], symmetric = True, normed = True)
        return graycoprops(glcm, 'correlation')[0,0]

    def contrast_fun(outRaster):
        """
        create contrast using the GLCM function 
        of Skimage
        """
        if len(outRaster.shape) == 1:
            outRaster = np.reshape(outRaster, (-1, sizeWindow)).astype('uint8')
        glcm = graycomatrix(outRaster, [1], [0], symmetric = True, normed = True)
        return graycoprops(glcm, 'contrast')[0,0]
        
    def  dissimilarity_fun(outRaster):
        """
        create dissimilarity_fun using the GLCM function 
        of Skimage
        """
        if len(outRaster.shape)== 1:
            outRaster = np.reshape(outRaster, (-1, sizeWindow)).astype('uint8')
            
        glcm = graycomatrix(outRaster, [1], [0], symmetric = True, normed = True)
        return graycoprops(glcm, 'dissimilarity')[0,0]

   

    # apply to moving window
    logging.info("Preparing Variance...")
    Variance      = ndimage.generic_filter(outRaster, np.var, size=sizeWindow)
    logging.info("Preparing Contrast...")
    Contrast      = ndimage.generic_filter(outRaster, contrast_fun, size=sizeWindow)
    logging.info("Preparing Dissimilarity...")
    Dissimilarity = ndimage.generic_filter(outRaster, dissimilarity_fun, size=sizeWindow)
    logging.info("Preparing Correlation...")
    Correlation   = ndimage.generic_filter(outRaster, correlation_fun, size=sizeWindow)
    logging.info("Preparing Homogenity...")
    Homogeneity   = ndimage.generic_filter(outRaster, homogeneity_fun, size=sizeWindow)
    logging.info("Preparing Entropy...")
    Entropy       = ndimage.generic_filter(outRaster, entropy, size=sizeWindow)
    

    return np.stack( (Variance, Contrast, Dissimilarity, Correlation, Homogeneity, Entropy) )

def perform_single_glcm(img, distances, angles, levels=256):

    glcm = graycomatrix(img.astype('uint8'), [distances], [angles], levels, symmetric=True, normed=True)

      # Compute GLCM properties
    contrast = graycoprops(glcm, 'contrast')[0,0]
    dissimilarity = graycoprops(glcm, 'dissimilarity')[0,0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0,0]
    energy = graycoprops(glcm, 'energy')[0,0]
    entropy = shannon_entropy(glcm)
    return np.stack((contrast,dissimilarity,homogeneity,energy,entropy))

def extract_raster(path,size,band=1):
    logging.info("Extracting Raster ...")
    img = rasterio.open(path)
    raster = img.read(band)
    logging.info(f"Previous Raster : {raster.shape}")
    raster = resize(raster,(size,size))
    logging.info(f"Changed Raster  : {raster.shape}")

    return raster

    