# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:36:11 2023

@author: tisso
"""


#range(n_initial,n_final-1,nb_de_pas)

n=int(input("Enter the value of n :"))
for i in range (n):
    q_1=i**2
    print (q_1)


n=int(input("Enter the value of n :"))
for i in range (1,n+1):
    q_1=i**2
    print (q_1)


n=int(input("Enter the value of n :"))
for i in range (1,n+1,2):
    q_1=i**2
    print (q_1)

sum=0
for i in range (6):
    sum=sum+i
    print(f"The value of sum is in each iteration: {sum} ")
print("The sum is valid {} ".format(sum))


prod=1 
for i in range (1,6):
    prod=prod*i
    print("The partial sum is {}".format(prod))
print("The total sum is valid {}".format(prod))


for i in range(4):
    for j in range (3):
        print("i = {}, j {}".format(i,j))


n=int(input("Enter a value:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print ("sum is {}".format(sum))
print("The sum is {}".format(sum))


n=int(input("Enter a value:"))
sum=0
for j in range (1, n+1):
    q=(j+1)/(j**2)
    sum=sum+q
    print(sum)
print ("The value of the sum is {: .2f}".format(sum)) #.2f donne les 2 premieère decimale après la virgule
#print (f"The value of the sum is {sum: .3f}") 

n=int(input("Enter a value:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)
print(f"The fact is {fact}")

for i in range(1,10):
    for j in range (1,10):
        print("{}{}".format(i,j))
        
for i in range(1,10):
    for j in range (1,10):
        if i!=j:
            print("{}{}".format(i,j))

a=int(input("Enter the nb of triangular nb you want:"))
for i in range (0,a+1):
    t=i*(i+1)/2
    print(t)

for i in range (1,10):
    for j in range (1,10):
        for k in range (1,10):
            print("{}{}{}".format(i,j,k), end=" ")

for i in range (1,10):
    for j in range (1,10):
        for k in range (1,10):
                if i+j+k ==22:
                    print("{}{}{}".format(i,j,k), end=" ")
for i in range (0,10):
    for j in range (0,10):
        for k in range (0,10):
                if (i**3+j**3+k**3) == (i*100+j*10+k):
                    print("{}{}{}".format(i,j,k), end=" ")

n=int(input("Enter an integer:"))
i=1
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")
        i=i+1

nb=int(input("Enter an integer value: "))
val=True
for i in range(2,nb):
    if nb%i==0 :
        val=False
   

if val==True:
    print(f"The value {nb} is a prime nb ")
else:
    print(f"The value {nb} is not a prime nb ")

n=int(input("Enter an integer value: "))
u1=0
u2=1
var=0
for i in range (0,n):
    var=u1+u2
    u1=u2
    u2=var
print(u2)