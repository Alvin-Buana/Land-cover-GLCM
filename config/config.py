# Place to put every important variables
import os
import numpy as np

datadir = './data'
sent2_folder_name = ' (Sent-2)'
sent1_folder_name = ' (Sent-1)'
img_size = 128
glcm_method = 2 #[each pixels : 1, all pixels : 2]

#glcm
glcm_save_path = datadir+"/glcm_features/"
distances = [1,2,3,4,5]
angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]

#model 
chosen_model = "Random Forest" #SVM or Random Forest

#Save model (need to create folder first)
model_saved_path = 'model_saved_path/'
