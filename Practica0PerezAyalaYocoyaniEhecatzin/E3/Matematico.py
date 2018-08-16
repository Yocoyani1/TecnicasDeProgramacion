# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 20:38:51 2018

@author: yocoy
"""

class Matematico:
    
    def __init__(self, matriz):
        self.matriz = matriz
        
    def matrizTranspuesta(self):
        matrizTranspuesta = []
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz[x])):
                matrizTranspuesta[y][x] = self.matriz[x][y]
        return matrizTranspuesta
                
    def traza():
        pass