from model.svm import modelSVC
from model.random_forest import modelRandomForest
from config.config import chosen_model

import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import train_test_split
import os
import glob
import pickle


from config.config import glcm_save_path,distances,angles,model_saved_path

def sent2_data_prep():
    datas = glob.glob(glcm_save_path+"*")
    distancess = distances
    # angless = angles
    for distance in distancess:
        # for angle in angless:
            
            df_group = []
            df = pd.DataFrame()
            for data in datas:
                # if data.split("_")[-2] == str(int(angle * 180 / np.pi)) and data.split("_")[-1].split(".")[0]==str(distance) :
                if data.split("_")[-1].split(".")[0]==str(distance) :

                    df_group.append(data)
            df2 = pd.DataFrame()
            for d in df_group:

                df1 = pd.read_csv(d,index_col=0)
                # concat the df first then pass onto a new dataframe
                df2 = pd.concat([df2,df1],axis=1)
                if df2.shape[1] == 21:
                    df=pd.concat([df,df2],axis=0)
                    df2 = pd.DataFrame()
                else:
                    df2 = df2.drop('label',axis=1)
               

            x = df.drop('label',axis=1)
            y = df['label'].values
            transformer = Normalizer()
            x = transformer.fit_transform(x)
            X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

            if chosen_model =="SVM":
                model = modelSVC(X_train,y_train)
            else:
                model = modelRandomForest(X_train,y_train)

            model.train()
            model.evaluate(X_test,y_test)
            # model.save(os.path.join(model_saved_path,"model_"+str(int(angle * 180 / np.pi))+"_"+str(distance)+".pkl"))
            model.save(os.path.join(model_saved_path,"model_"+str(distance)+".pkl"))
        

