import os 
from config.config import datadir

def checkFolder(name):
    if not os.path.exists(name):
        os.mkdir(os.path.join(name))