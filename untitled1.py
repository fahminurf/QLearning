# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:04:57 2019

@author: King
"""
import pandas as pd
import numpy as np


#import data

data = pd.read_csv('DataTugas3ML2019.txt', sep="\t", header=None)

#inisiasi tabel Q
mintak = np.float('-inf')
 
QtabN=[]
QtabE=[]
QtabS=[]
QtabW=[]


for i in range (len(data)):
    for j in range(len(data)):
        if (i==0):
            QtabN.append(mintak)
        else:
            QtabN.append(0)

for i in range (len(data)):
    for j in range(len(data)):
        if (j==14):
            QtabE.append(mintak)
        else:
            QtabE.append(0)

for i in range (len(data)):
    for j in range(len(data)):
        if (i==14):
            QtabS.append(mintak)
        else:
            QtabS.append(0)


for i in range (len(data)):
    for j in range(len(data)):
        if (j==0):
            QtabW.append(mintak)
        else:
            QtabW.append(0)
            

            
Qtab = np.array([QtabN,QtabE,QtabS,QtabW])

#Qtab = np.zeros_like(r)


#array untuk mengambil indeks
kun= np.arange(225)
kun = kun.reshape(15,15)
#print("Reverse array:")
kun = kun[::-1]


tew=pd.read_csv('titikkelokasi.txt', header = None, sep='\t')

kuncoro = pd.DataFrame(tew)
apaanya= pd.DataFrame(kun)

repostab=[]
for i in range(15):
    for j in range(15):
        repostab.append(np.array([data[i][j],apaanya[i][j]]))
        

gamma = 1
alpha = 1


#cari reward
def reward(state):
    rew = 0
    point=0
    for k in range(224):
        if repostab[k][1]==state:
            rew=repostab[k][0]
            point=repostab[k][1]
    return rew,point

#cari step 
    
rd0=0
statenow= 0
while True:
    rd=np.random.randint(0,3)
    while (Qtab[rd][statenow]== mintak):
        rd=np.random.randint(0,3)
    if (rd0 == 0 and rd == 3):
        while (rd == 3):
            rd=np.random.randint(0,3)
    elif (rd0 == 1 and rd == 2):
        while (rd==2):
            rd=np.random.randint(0,3)
    elif (rd0==2 and rd == 1):
        while (rd==1):
            rd=np.random.randint(0,3)
    elif (rd0 == 3 and rd == 0):
        while (rd == 0):
            rd=np.random.randint(0,3)
    rd0=rd
      
    if rd == 0:
        rew,point=reward(statenow+15)
        sacc=point
        print()
        print('North')
#        
    elif rd == 1:
        rew,point=reward(statenow+1)
        sacc=point
        print()
        print('East')
#       
    elif rd == 2:
        rew,point=reward(statenow-15)
        sacc=point
        print()
        print('South')
#        
    elif rd == 3:
        rew,point=reward(statenow-1)
        sacc=point
        print()
        print('West')
    
    
    Qtab[rd][statenow]=Qtab[rd][statenow]+alpha*(rew+gamma*(max(Qtab[:,sacc]))-Qtab[rd][statenow])
    statenow=sacc
     
    print('state :',sacc)
    print('reward : ',Qtab[rd][statenow])
    if (Qtab[rd][statenow]== 500): 
        break

        
        
        