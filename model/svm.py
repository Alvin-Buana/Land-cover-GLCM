from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import logging
import pickle

class modelSVC():
    def __init__(self,X,y,gamma = 'auto'):
        self.X = X
        self.y = y
        self.model = SVC(gamma=gamma)


    def train(self):
        logging.info("Model SVM in training...")
        self.model.fit(self.X, self.y)
        logging.info("Model SVM done training...")

    def evaluate(self,x_test,y_test):
        self.y_pred = self.model.predict(x_test)
        self.result = accuracy_score(y_test, self.y_pred)
        logging.info(f"the result of the model is {self.result}")
    
    def predict(self,X_test):
        logging.info("Model SVM predicting...")
        self.res = self.model.predict(X_test)
        logging.info("Model SVM done predicting...")
        return self.res
    def save(self,name):
        with open(name, 'wb') as f:
            pickle.dump(self, f)
        logging.info(f"saving model on {name}")

    
