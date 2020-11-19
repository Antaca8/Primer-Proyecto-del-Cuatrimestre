# -*- coding: utf-8 -*-
'''
Created on 12 oct. 2020

@author: anton
'''
from audiencias import *

def test_lee_audiencias_GH():
    AUDIENCIAS_GH = lee_audiencias('../data/GH.csv')
    print(AUDIENCIAS_GH[:20])
    suma = 0
    for edicion, audiencia in AUDIENCIAS_GH:
        print(edicion, "-->", audiencia)
        suma+= audiencia
    
    print(suma/len(AUDIENCIAS_GH))

    ediciones = calcula_ediciones(AUDIENCIAS_GH)
    print(ediciones)
def test_lee_audiencias_GH_VIP():
    AUDIENCIAS_GH_VIP = lee_audiencias('../data/GH_VIP.csv')
    print(AUDIENCIAS_GH_VIP[:20])
    ediciones = calcula_ediciones(AUDIENCIAS_GH_VIP)
    print(ediciones)
    
if __name__=='__main__':
    
    test_lee_audiencias_GH()
    #test_lee_audiencias_GH_VIP()