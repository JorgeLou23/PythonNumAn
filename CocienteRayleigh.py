# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:56:31 2018

@author: ciencias
"""

from pylab import*
from scipy import linalg

nombre='sistema3.txt'
myfile=open(nombre)

n=int(myfile.readline())
a=zeros((n+1,n),float64)
b=zeros(n, float64)
x=zeros(n, float64) 
y=zeros(n, float64)


a=loadtxt(nombre,skiprows=1)



myfile.close

print('\n Matriz:','\n',a,'\n')
print('\n', 'Vector: ','\n', b,'\n')

itmax=100
tol=1.e-9
l=5.7

for i in range(0,n-1):
    x[i]=1
x=x/norm(x,2)
for it in range(1,itmax):
    lu, piv =linalg.lu_factor(a-l*eye(n))
    y=linalg.lu_solve((lu,piv), x)
    dif=min(norm(y/norm(y,2)-x,2),norm(y/norm(y,2)+x,2))
    x=y/norm(y,2)
    l=dot(dot(x,a),x)
    if dif<tol*norm(y,2):
        break


    
    
print('Número de iteraciones: ', it)
print('Valor propio más próximo: ', l)
print('Vector propo asociado a dicho valor: ', x)
print('error: ', dif)