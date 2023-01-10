# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 15:29:06 2023

@author: Chamakh Feriel
"""
from functools import wraps

#creation du singleton
def singleton(cls):
    instance={}
    @wraps(cls)
    def wrapper(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return wrapper