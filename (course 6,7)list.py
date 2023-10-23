# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:36:11 2023

@author: tisso
"""


us_president_list=['Joe Biden', 'Donald Trump','Barack Obama','Nixon','George W Bush']
us_president_list.append('Bill Clinton')
us_president_list.remove('Joe Biden')
us_president_list[3]='Pilou'
for president in us_president_list:
    print(president)
    
    
smooth=[3.14, 7, -2+3j, 'water', False, [1,2]]
print(smooth)
long_smooth=len(smooth)
print(long_smooth)
print(smooth[::2])
print(smooth[5][1])


n=10
sum=0
for i in range  (1,n+1) :
    sum=sum+1/i
print(sum)


n=int(input ("Enter a n value : "))
thelist=[]
for i in range(1,n+1):
    thelist.append(i)
Sn=sum(thelist)

    

nombre=int(input("Entrez votre numero : "))
liste_de_nombre=[]
for i in range (1,nombre+1):
    liste_de_nombre.append(i**2)
print(liste_de_nombre)


nom=[]
note=[]

name="a"
while (name!=""):
    name=input("Enter a name : ")
    if(name!=""):
        nom.append(name)
        x=int(input("Enter his grade : "))
        note.append(x)

somme=0
for i in range (len(note)):
    somme+=note[i]
if (len(note)!=0):
    note.append(somme/len(note))
print (nom)
print (note)



nom=[]
note=[]

name='a'
while name!="":
    name=input("Enter a name : ")
    if name!="":
        nom.append(name)
        x=int(input("Enter a grade : "))
        if x!="":
           note.append(x)

somme=0
for i in range (len(note)):
    somme=somme+note[i]
print(nom)
print(note)
print(f"the average is : {somme/len(note)}")
print (note[::2])



    
    
#EXO 7

values=[]
somme=0
x=0
while x!="" :
    x=int(input("Enter a value : "))
    if x!="" :
        values.append(x)

for i in range(len(values)):
    
    somme=somme+values[i]
print(f"the average is {somme/len(values)}")
        


#exo8


names=[]
name=(input("Enter a name : "))

while name!="" : 
    names.append(name)
    name=(input("Enter a name : "))


for i in range (len(names)) :
    print(f"Hi {names[i]}")
    

names=input("Enter a list of anmes separated by spaces : ")
list_names=names.split()
for name in list_names:
    print("Hi"+name)
print("Welcome all{}".format(len(list_names)))



#exo 9

Elements=['H','C','N','O','S','Cl']
Atomic_mass=[1.008,12.011,14.007,15.999,32.065,35.453]
somme=0

for i in range (len(Elements)) :
    x=int(input("Enter the number of "+Elements[i]+" you want : "))
    Atomic_mass[i]=float(Atomic_mass[i])
    somme=somme+x*Atomic_mass[i]
print(somme)

    
    


#Exo 10

x=int(input("Enter the maximum degree of your polynomial : "))
coefficient=[]
for i in range (x+1) : 
    y=int(input(f"Enter the coefficient of the {i} element : "))
    coefficient.append(y)
    
z=int(input("What is the value of x of your polynomial : "))
j=0
for i in range(len(coefficient)):
    j=j+coefficient[i]*z**i
    
print (j)


#correction

n=int(input("Enter the degree of the polynomial : "))
coef=input("Enter the coefficient in order separated by a space:").split()
x=float(input("Enter the value of x where you want to calculate P(x) : "))
sum=0
for i in range(n+1):
    sum+=int(coef[i])*x**i
print("The function result is {}".format(sum)) 










