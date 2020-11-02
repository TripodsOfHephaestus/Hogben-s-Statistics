# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:07:10 2020

@author: caval

The special permutation of the case 3 and general example of p momments

topbun on previous "bistro.py" starts at n=4
For the special case of number 3 top bun is in a 1:2:1 ratio 
Using this ratio and the square grid we can count all permutations of 3
in regards to d**2

"""
s3=2
ratio=[1,2,1]
d=[0]
three_perm=[]
ds=2
#in the special case of three d is given by general rule of topbun
for i in range(0,4):
    d.append(ds)
    ds+=2
    

#build steps to move 
for i in range(0,3):
     three_perm.append(s3*ratio[i])
     
#General note on the special case of n<10 1, 1+1, 2+1, 2**2, 2**2+1, 2**2+2, 2**3, 2**3+1
#this is to build the grid, grid walk is equals to ds, just for general information on grid
#form and the properties of 1,2,3 

grid=[]
for i in range(1,10):
    grid.append(i)
    
#All permutations of three
All3p=[]
k=2
for i in range(0,3):
    All3p.append(k)
    k+=three_perm[i]
    
#order ratio
    

indexj=0  
ratio2=[1,2,1]
while indexj<len(ratio)-1:
    if ratio[indexj]>ratio[indexj+1]:
        ratio2[indexj]=ratio[indexj+1]
        ratio2[indexj+1]=ratio[indexj]
    indexj+=1
    
#ajusting to get correct ratio, in essence is the same thing
for i in range(len(ratio2)):
    ratio2[i]=ratio2[i]*2
    
ratio2[2]=1

#Count all permutations of the special number 3 in regards to d**2
tsquarednumb=[]
tot=()
for i in range(0,3):
  #  print(ratio2[i], All3p[i])
    tot=(ratio2[i], All3p[i])
    tsquarednumb.append(tot)
    
     
#d2/n

d2n=[]

for i in range(len(d)):
   d2n.append(d[i]/3)
#   


##get y - just an interesting note n here can be written as 3! or 1+2+3
All3p.insert(0,0)
y=[]
listtest2= [x[1] for x in tsquarednumb]
listtest2.insert(0,0)
listtest= [x[0] for x in tsquarednumb]
listtest.insert(0,0)
counts=0
for i in range(len(d)):
    counts=0
    if d[i]in All3p:
            counts=listtest[listtest2.index(d[i])]
            print(d[i], counts)      
            y.append(counts)
#unordered
y.insert(0,1)#for the one zero    
for i in range(len(y)):
    y[i]=y[i]/6
 
sumd2=All3p[3]/2

#p for special 3
plist=[]
for i in range(len(All3p)):
   p=1-(All3p[i]/sumd2)
   plist.append(p)
   
#for variance of d**2 when y works
t=0
#ordery
y=[.1666, .3333, 0, .3333, .16666]
for i in range(len(y)):
    t+=y[i]*d[i]**2


#for variance of p
Vp=1/(sumd2)**2*All3p[3]





        
        
        


          
    
    
        
    

    
    
    

