# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

from pylab import*

nombre='ejemplo1.txt'

myfile=open(nombre)

n=int(myfile.readline())
a=zeros((n+1,n),float64)
b=zeros(n, float64)
x=zeros(n, float64)
y=zeros(n, float64)

a=loadtxt(nombre,skiprows=1)
b=a[n]

a=delete(a,n,axis=0)

myfile.close

print('\n Matriz:','\n',a,'\n')
print('\n', 'Vector: ','\n', b,'\n')

itermax=50
eps=1.e-10
toldiv=1.e+5
tol=1.e-15
fin='nofin'

for it in range(itermax):
    for k in range(0,n):
        y[k]=(b[k]-dot(a[k,0:k],y[0:k])-dot(a[k,k+1:n],x[k+1:n]))/a[k,k]
    dif=norm(x-y,2)

    if dif<=tol:
        print('convergencia alcanzada en la iteración',k)
        print('la solución es:')
        print(y)
        print('error: ', dif)
        fin='conv'
        break
    
    elif dif>toldiv:
        print('metodo divergente en la iteración', k)
        fin='div'
        break
        sys.exit()
        
    x=copy(y)
if fin=='nofin':
    print('no se ha alcanzado la convergencia tras ', itermax, ' iteraciones')
    print('la aproximación de la solución es: ', y)
    print('error: ', dif)

    
    
    
    