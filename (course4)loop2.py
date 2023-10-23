# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:36:11 2023

@author: tisso
"""


num=int(input("Enter an integer value:"))

while num>0:
    res=num//3
    print('The integer division of {} by 3 gives: {}'.format(num,res))
    num=int(input("Enter an integer value:"))

print("We're done")



num=int(input("Enter an integer value:"))
ndiv=1

while ndiv<num:
    res=num//ndiv
    print("The integer division of {} by {} gives: {}".format(num,ndiv,res))
    ndiv=ndiv+1 

print("We're done")
print("Total number of division: {}".format(ndiv))



num=int(input("Enter an integer value:"))
ndiv=0

while ndiv<num:
    res=num//3
    print("The integer division of {} by 3 gives: {}".format(num,res))
    ndiv=ndiv+1 #ou ndiv+=1
    print("Number of division so far: {}".format(ndiv))
    num=int(input("Enter an integer value:"))

print("We're done")
print("Total number of division: {}".format(ndiv))


num=1
ndiv=0

while num>0 and num<211:
    if num%3==0:
        print(f"The number is {num}")
        ndiv=ndiv+1
    num=num+1
    
print("We're done")
print("Total number of division: {}".format(ndiv))


num=0
i=0
while num<=10:
     i=i+num
     num=num+1
print(i)



i=0
sum=0
while i<10:
    num=int(input("Enter an integer value:"))
    sum=sum+num
    i=i+1

average=sum//10
print(average)



i=1
while i<=4:
    print("*"*i)
    i=i+1
# avec boucle for     
x=int(input("nb of line: "))
nb=0
for i in range (x):
    nb+=1
    print(nb*"*")


num=int(input("Enter an integer value:"))
f=num
r=1
while f!=0:
    r=r*f
    f=f-1
print("Factorial of",num,"is:",r)


name='Jesaa29Roy'
size=len(name)
i=0 
while i <size:
    
    if name[i].isdecimal():
        break;
    
    print(name[i],end=' ')
    i=i+1
print("\nThe execution has stopped")


name='Jesaa29Roy'
size = len(name)
i=-1

while i<size-1:
    i=i+1
    
    if not name[i].isalpha():
        continue
    print(name[i],end=' ')

    

n=int(input("Enter the value of n: "))
for i in range (n):
    q_i=i**2  
    print(q_i)