# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 20:40:57 2018

@author: yocoy
"""
import numpy as np

def fun(x):
	
	x = np.exp(-x)+np.log(x)
	return x

def dfun(x):
	
	x = -np.exp(-x)+(1/x)
	return x

    
def main ():
	
    pass
	
main()

