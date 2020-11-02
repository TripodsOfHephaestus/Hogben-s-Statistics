# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:42:39 2020

@author: caval
"""

#maybe make it fancier
fseries=[345678910]

def factor(n,j):
    j=n*j
    
    if n==1:
        return j
    
    return factor(n-1,j)

fseries1=[]
fseries2=[]
fseries3=[]
f2=1

for i in range(len(fseries)-1):
    fseries1.append(fseries[i])
    test=fseries[i+1]
    f2=factor(test, 1)/2
    fseries2.append(f2)
    
for i in range(len(fseries)-2):
   
    test=fseries[i+2]
    f3=factor(test, 1)/6
    fseries3.append(f3) 

    
    
    
print (factor(5,1)) 


"""
central polygon

"""
k=3
J=3

centeredsquare=[]
centeredpentagonal=[]
centeredhex=[]
for i in range(10):
    centeredsquare.append(1+4*J)
    centeredpentagonal.append(1+5*J)
    
    J=J+k
    k+=1
  
j=10
k2=5
for i in range(10):
    
    centeredhex.append(1+6*j)
    j=j+k2
    k2+=1
    

"""

squares
square one use squares for 2Fn
square two uses 2fn for squares
square three uses odds and evens to make squares

"""
square1=[]
start=2*2-1
for i in range(3,10):
    k=i*i-start
    start=k
    square1.append(k)
    
square2=[]

for i in range(len(square1)-1):
    square2.append(square1[i]+(square1[i+1]))
    
square3=[]
start1=4
start2=12
addj=5

for i in range(0,20):
    start1=start1+4
    start2=start2+addj
    addj=addj+2
    
    squarethree=start1+start2
    square3.append(squarethree)
    
    

    
    
    
    
    
