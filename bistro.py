# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 17:28:30 2020
@author: caval
Sum of Sqaured Differences for Spearmans Rank Association Index -
For a sequence with perfect corresponding set

1 2 3 4 5 6 7 8 9 10
10 9 8 7 6 5 4 3 2 1

p=-1 total would correspond to sqd[n]
mean value given by sqd[n]/2
value of p sqd[n]/mean
note sqd starts @ n=6 which coincides when Pearson type 2 merges with the normal distribution

"""

topbun=10
bistromeats=20
lowerbun=40
sqd=[]
sqd2=[]  #for recursive
order=3 #for recursive
bistro=0


for i in range(0,10):
    bistromeats+=topbun
    topbun+=2
    lowerbun+=bistromeats
    bistro=lowerbun
    sqd.append(bistro)
    
topbun2=10
bistromeats2=20
lowerbun2=40
sqd2=[]  #for recursive
order=10 #for recursive
bistro2=0
    
def bistromaking(topbun2, bistromeats2,lowerbun2, order, bistro2, sqd2):
    if order >0:
        bistromeats2+=topbun2
        lowerbun2+=bistromeats2
        bistro2=lowerbun2
        sqd2.append(bistro2)
      
        return  bistromaking(topbun2+2, bistromeats2,lowerbun2, order-1, bistro2, sqd2)
    else:
        return sqd2
        
    

print (bistromaking(topbun2, bistromeats2, lowerbun2, order, bistro2, sqd2))


