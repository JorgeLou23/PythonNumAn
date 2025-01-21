# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:19:23 2018

@author: ciencias
"""

from pylab import*
from scipy import linalg

nombre='ejemplo10.txt'
myfile=open(nombre)

n=int(myfile.readline())
a=zeros((n+1,n),float64)
b=zeros(n, float64)
x=zeros(n, float64) 
y=zeros(n, float64)


a=loadtxt(nombre,skiprows=1)


myfile.close

print('\n Matriz:','\n',a,'\n')

itmax=100
tol=1.e-6
l=1

lu, piv =linalg.lu_factor(a-l*eye(n))
for i in range(n):
    x[i]=1
x=x/norm(x,2)
for it in range(1,itmax):
    y=linalg.lu_solve((lu,piv), x)
    dif=min(norm(y/norm(y,2)-x,2),norm(y/norm(y,2)+x,2))
    x=y/norm(y,2)
    if dif<tol*norm(y,2):
        break
l=dot(dot(x,a),x)

    
    
print('Número de iteraciones: ', it)
print('Valor propio más próximo: ', l)
print('Vector propo asociado a dicho valor: ', x)
print('error: ', dif)
