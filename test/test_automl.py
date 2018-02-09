# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:15:42 2017

@author: mvanoudh
"""

import logging
import numpy as np
import pandas as pd
import time
from numpy.random import seed

from sklearn2.datasets import get_titanic, get_house_prices, get_iris, get_boston
from sklearn2.automl import get_best_model

pd.options.display.width = 160

logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s')
logging.getLogger().setLevel(level=logging.INFO)

seed(0)


def getsize(obj):
    from pympler.asizeof import asizeof
    from sys import getsizeof
    return getsizeof(obj) / 1024, asizeof(obj) / 1024


def get_titanic_raw():
    return get_titanic(True, False)


def print_sm(sm):
    print('Pipeline:')
    for s in m.best_estimator_.steps:
        print('  ', s[1])


#for data_func in [get_titanic_raw]:
#    print('dataset:', str(data_func).split()[1])
#    x, y = data_func()    
#    m = get_best_model(x, y, None, None, 1) 
#    print_sm(m)
    
#df = get_titanic(False, False)

#from sklearn.preprocessing import Imputer
#
#Imputer().fit_transform(df)
