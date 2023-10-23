# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:13:34 2023

@author: tisso
"""


import numpy as np
import math


a=np.array([1,2,3],dtype='int32')
print(a)
b=np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]],dtype='int32')
print(b)

a.ndim#get dimension
b.shape#getshape
a.dtype#get type
a.itemsize#get size
a.nbytes#get total sizes
a.size#get total sizes


c=np.array([[9.0,'c',7.0],[6.0,9.0,4.0]])
print(b)
c.shape
c.dtype
d=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(d)
print(d[1,5])
print(d[0,:])#get la ligne 
print(d[-1,:])
print(d[0,1:-1:2])# premier row, 2e element in a row,3e stop index, 4e stop size
d[1,5]=20
d[:,2]=[1,2]
print(d)

np.zeros((2,3))

b=np.array([[[1,2],[3,4],[7,8]]])
print(b)

np.full((2,2),99)
np.full_like(a,4)
np.random.rand(4,2)
#np.random.radint(-4,8,size=(3,3))#le premier  on specifie le min et le max et le deuxieme c est la taille

np.identity(5)#matrice identite

arr=np.array([[1,2,3]])
r1=np.repeat(arr,3,axis=1)
print(r1)

output=np.ones((5,5))
print(output)

z=np.zeros((3,3))
z[1,1]=9
print(z)

output[1:-1,1:-1]=z
print(output)


npoints=21
values=np.linspace(10,30,npoints)
values[6]=1
print(values)



np.cos(a)


a=np.ones((2,3))
print(a)

b=np.full((3,2),2)
print(b)

np.matmul(a,b)


d=np.random.randint(-4,2,size=(2,3))
print(d)
e=np.random.randint(-5,5,size=(3,2))
print(e)
print(np.matmul(d,e))
print(np.matmul(e,d))


f=np.random.randint(-10,10,size=(4,4))
print(f)
g=np.random.randint(-4,10,size=(3,3))
print(g)
print(np.linalg.det(f))
print(np.linalg.det(g))

stats=np.array([[1,2,3],[4,5,6]])
stats
np.min(stats)
np.min(stats, axis=0) 
np.min(stats,axis=1) 
np.max(stats)

print(np.sum(stats))
print(np.sum(stats), axis=0)

arr=np.array([[1,2,3]])
r=np.repeat(arr,3,axis=-2)
print(r)


#ex1
angles=[0,math.pi/4,math.pi/2,3*math.pi/4,math.pi]
angles=np.array(angles)
sin_angle=np.sin(angles)
print("Angles:{}".format(angles))
print("Sinus:{}".format(sin_angle))

#ex2
import numpy
npoints=21
values=np.linspace(-2.0,2.0,npoints)
print(values)

#ex3 
vect=np.arange(9)
print(vect)

npoints=21
values=np.linspace(10,20,npoints)
values[6]=1
print(values)




