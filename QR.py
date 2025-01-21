# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:07:16 2018

@author: ciencias
"""
#Jorge Lou Franco

from pylab import*
from scipy import linalg

nombre='sistema3.txt'
myfile=open(nombre)

n=int(myfile.readline())
a=zeros((n,n),float64)

a=loadtxt(nombre,skiprows=1)

myfile.close

itmax=400
tol=1.e-12

for it in range(1,itmax+1):
    q,r=qr(a)
    a=dot(r,q)
    dif=0
    for j in range (0,n-1):
        for i  in range (j+1,n):
            #print(i,j)
            dif=max(dif,abs(a[i][j]))
            #print(a[i][j])
    #print(dif)
    #print(a)
    if dif<tol:
        break

print('Número de iteraciones: ', it)
print('\n Matriz:','\n',a,'\n')
for i in range(n):
    print('Valor propio: ', a[i][i])
print('error: ', dif)

