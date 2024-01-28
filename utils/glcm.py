

from skimage.feature import graycomatrix, graycoprops
import pandas as pd
import logging
import os


def glcm(path):
    items = os.listdir(path)
    items.sort()
    df = pd.DataFrame(columns =["contrast","homogeneity","energy","entropy"])
    distancess = [1, 2, 3, 4,5,6,7,8,9,10]  # Specify the distances to compute
    angless = [0, np.pi/4, np.pi/2, 3*np.pi/4]  # Specify the angles to compute
    if 
    for disc in tqdm_notebook(distancess,desc='Distance'):
    for ang in tqdm_notebook(angless,desc='Angle'):
        word = str(int(ang * 180 / np.pi))+"_"+str(disc)
        df = pd.DataFrame(columns =["contrast_"+word,"homogeneity"+word,"energy"+word,"entropy"+word])
        for item in tqdm_notebook(items,desc = 'Item'):
        img = cv2.imread(path+item,0)
        parts =[]
        distances = [disc]
        angles = [ang]
        levels=256
        glcm = graycomatrix(img, distances, angles, levels, symmetric=True, normed=True)

        # Compute GLCM properties
        contrast = graycoprops(glcm, 'contrast')
        # dissimilarity = graycoprops(glcm, 'dissimilarity')
        homogeneity = graycoprops(glcm, 'homogeneity')
        energy = graycoprops(glcm, 'energy')
        entropy = shannon_entropy(glcm,'entropy')
        df.loc[len(df)] =[contrast[0][0],homogeneity[0][0],energy[0][0],entropy]

        df.to_csv("data/glcm_features/"+str(distances[0])+"_with_"+str(int(angles[0] * 180 / np.pi))+"_degree.csv")