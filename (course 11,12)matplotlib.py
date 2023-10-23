# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:11:01 2023

@author: tisso
"""

import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(-2,2,101)
y=x**2
print(x)                            

plt.plot(x,y)
plt.show()

x=np.linspace(0,3*np.pi,500)
plt.plot(x,np.sin(x**2))
plt.title('A simple chirp')




x=np.linspace(-2,2,101)
y=x**2

plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-1.5, 1.5)
plt.ylim(-0.5, 2.5)
plt.title("Chart Title")
plt.plot(x, y)
plt.show()


x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y=x**2
plt.plot(x,y)
y2 = x**4
plt.plot(x, y2)
plt.show()





x=np.linspace(-2,2,101)
plt.xlabel("x")
plt.ylabel("f(x)")
y=x**2
plt.plot(x, y, label = "x^2")
y2 = x**4
plt.plot(x, y2, label = "x^4")
plt.legend()
plt.show()



x=np.linspace(-2,2,11)
plt.xlabel("x")
plt.ylabel("f(x)")
y2=x**2
plt.plot(x, y2, 'g',label = "x**2")
y3 = x**3
plt.plot(x, y3, 'ro', label = "x**3")
y4=x**4
plt.plot(x, y4, 'b.', label='x**4')
plt.legend()
plt.show()



Num=int(input("Enter the number of point you want to draw : "))
x=np.linspace(-1,1,Num)
plt.xlabel("x")
plt.ylabel("f(x)")
y=np.cos(2*np.pi*x)
plt.plot(x,y,label='Body function (2pix)')
plt.legend()
plt.savefig("cos2pix.png")
plt.show()




Num=int(input("Enter the number of point you want to draw : "))
x=np.linspace(-1,1,Num)
plt.xlabel("x")
plt.ylabel("f(x)")
y=np.cos(2*np.pi*x)
plt.plot(x,y,label='Body function cos(2pix)')
y2=np.sin(2*np.pi*x)
plt.plot(x,y2,label='Body function sin(2pix)')
plt.legend()
plt.savefig("trigonometric.png")
plt.show()



#exo3
m=True
while m:
    try:
        n=int(input("Enter the number of point : "))
        
    except ValueError as e:
            print("pas de float que des int")
    else:
        m=False
        x=np.linspace(0,4,n)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        y=np.sin(np.pi*x)*np.sin(20*(np.pi)*x)*np.exp(-x)
        plt.plot(x,y,label="sin(pi*x)sin(20pi*x)*e^(-x)")
        plt.legend()
        plt.show()

#exo 4    

n=int(input("Enter the number of point to draw : "))
T=float(input("Enter the temperature K : "))
R=0.08206
Vm=np.linspace(2,10,n)

plt.xlabel("Molar volume")
plt.ylabel("Pressure")
plt.title("Isotherme")
p=R*T/Vm
plt.plot(Vm,p)
plt.savefig("isotherme.jpg")
plt.show()


#exo 2

n=int(input("Enter the number of point for the function: "))
x=np.linspace(0,3,n)
plt.xlabel("x")
plt.ylabel("f(x)")
y=np.sin(3*np.pi*x)*np.exp(-x)
plt.plot(x,y,label='sin(3pix)e^(-x)')
y2=np.exp(-x)
plt.plot(x,y2,label='e^-x')
plt.title("sin(3pix)e-x and e-x")
plt.legend()
plt.show()

#exo1
xo=int(input("Enter xo: "))
s=float(input("Enter s: "))
d=int(input("Enter the number of point for the function: "))
f=int(input("Enter the number of point for the function: "))
n=int(input("Enter the number of point for the function: "))
x=np.linspace(d,f,n)
plt.xlabel("x")
plt.ylabel("f(x)")
y=(1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - xo) / s)**2)
plt.plot(x,y)
plt.title("Fonctioin de gauss")
plt.legend()
plt.show()


#exo3

n = int(input("How many?"))
for i in range (0,n):
    x = np.linspace(-1,1,100)
    s = float(input("s"))
    x0 = float(input("x0"))
    y=(1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - xo) / s)**2)

    a = input("line : ")
    nom = input("name ? ")
    plt.plot(x,y,a,label = nom)

plt.title("Gaus")
plt.legend()
plt.show()








