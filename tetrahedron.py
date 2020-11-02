# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:37:25 2020

@author: caval
"""
import numpy as np

#tetrahedron

def position(p1,p2,tetras):
    while p1>0:
        tetras.append(p1)
        return position(p1-1, p2, tetras)
    if p1==0:
        p2=p2-1
        p1=p2
        return position(p1, p2, tetras)
    if p2==0:
        return(p1, p2, np.sum(tetras))
tetras=[]        

t=[]
position(10,10,tetras)
    
t=np.sum(tetras)


#triangular
#prior n=5 1,3,5+1
n=7
k=3
j=3

triangular=[]

for i in range(0,100):
    n=n+2
    j=k+j
    k=k+1
    
    triangular.append(n)
    triangular.append(j)
    triangular.append(n+j)
    
    


