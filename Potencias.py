# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:15:38 2018

@author: ciencias
"""

from pylab import*

nombre='ejemplo5.txt'
myfile=open(nombre)

n=int(myfile.readline())
a=zeros((n+1,n),float64)
b=zeros(n, float64)
x=zeros(n, float64) 
y=zeros(n, float64)


a=loadtxt(nombre,skiprows=1)


a=delete(a,n,axis=0)

myfile.close

print('\n Matriz:','\n',a,'\n')
print('\n', 'Vector: ','\n', b,'\n')

itmax=100
tol=1.e-6

for i in range(0,n-1):
    x[i]=1
x=x/norm(x,2)

for it in range(itmax):
    y=dot(a,x)
    l=dot(x,y)
    dif=norm(y-l*x,2)
    x=y/norm(y,2)
    if dif<tol*norm(y,2):
        break
    
print('Número de iteraciones: ', it)
print('Valor propio dominante: ', l)
print('Vector propo asociado a dicho valor: ', x)
print('error: ', dif)
        
        
    
