# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:36:11 2023

@author: tisso
"""



num=input("Enter an integer")
num=int(num)
if num <5:
    print("It's less than five")
else:
    print("It's greater than or equal to five")
    

num=int(input("Enter the number:"))
if num%2==0:
    print("The number {} is an even number ".format(num))
else:
    #print("The number {} is an odd number".format(num))
    print(f"The number {num} is an odd number")
    

marks=float(input('Enter a grade(out of 10):'))  
if marks<40:
    print('The student has failed and got an F')
elif marks>40 and marks<=50:
    print('The student has passed marginaly and got an E grade')
elif marks>=50 and marks <=75:
    print("The student has passed with C grade")
elif marks >=75 and marks <=90:
    print("The student has done well and has scored B grade")
else:
    print("The student has done excellent and passed with Distinction, A grade")
                     

weight=float(input('Enter your weight:'))
height=float(input('Enter your height'))   
BMI=weight/(height**2)
if BMI<18.5:
    print("Your BMI is {} and you are in underweight".format(BMI))
elif BMI>=18.5 and BMI<25:
    print("Your BMI is {} and you are in normal weigth".format(BMI))
elif BMI>=25 and BMI<30:
    print("Your BMI is {} and you are in overweight".format(BMI))
else:
    print("Your BMI is {} and you are in obesity".format(BMI))
    

n1= int(input("Enter a natural number:"))
n2= int(input("Enter an other natural number:"))
n=n1/n2
r=n1%n2
if r==0:
    print("The number {} is divisible by {} and the quotient is {}".format(n1,n2,n))
else:
    print("The number {} is not divisible by {} but the remainder is {} ".format(n1,n2,r))



n1= int(input("Enter a natural number:"))
n2= int(input("Enter an other natural number:"))
if n1>n2:
    print("The number {} is bigger than {}".format(n1,n2))
elif n1<n2:
    print("The number {} is bigger than {}".format(n2,n1))
else:
    print("The number {} is equal to {}".format(n1,n2))
 

a= int(input("Enter your unit:"))
if(a<100):
    print("You will have no charge ")
elif a>=100 and a<200:
    p=5*(a-100)
    print("You have {}unit so your bill will be Rs{}".format(a,p))
else:
    p=10*(a-200)+100*5
    print("You have {}unit so your bill will be Rs{}".format(a,p))