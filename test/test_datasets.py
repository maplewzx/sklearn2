# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:46:47 2017

@author: mvanoudh
"""


from sklearn2.datasets import get_iris, get_boston, get_titanic
from sklearn2.utils import print_summary


x, y = get_iris()
print_summary(x)

x, y = get_boston()
print_summary(x)

x, y = get_titanic()
print_summary(x)

