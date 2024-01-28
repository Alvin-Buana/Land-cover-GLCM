from sklearn.svm import SVC
import logging

class modelSVC():
    def __init__(self,X,y,gamma = 'auto'):
        self.X = X
        self.y = y
        self.model = SVC(gamma=gamma)

    def train(self):
        logging.info("Model SVM in training...")
        self.model.fit(self.X, self.y)
        logging.info("Model SVM done training...")

    def evaluate(self):
        pass
    
    def predict(self,X_test):
        logging.info("Model SVM predicting...")
        self.res = self.model.predict(X_test)
        logging.info("Model SVM done predicting...")
        return self.res
    
