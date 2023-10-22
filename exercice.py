# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:55:26 2023

@author: tisso
"""
import math as m
import pandas
import numpy as np

'''
R=0.08796
n=0.5
T=311
p=8.9
print ("At temperature {} K the pressure is {} atm.".format(T,p))
a=2
b=3
area=a*b
print("The area of the edege of rectangle {} and {} is valid {}.".format(a,b,area))

a=4
b=2
print(complex(a,b))

R=0.08206
n=input ("Enter the number of moles:")
n=float(n)
T=input ("Enter the temperature in K:")
T=float(T)
V=input ("Enter the volume in L:")
V=float(V)
p=n*R*T/V
print("Gas pressure is{} atm".format(p))

R=0.08206
n=float(input ("Enter the number of moles:"))
T=float(input ("Enter the temperature in K:"))
V=float(input ("Enter the volume in L:"))
p=n*R*T/V
print("Gas pressure is{} atm".format(p))



ang=float(input("Enter an angle in sexadesimal degrees :"))
ang_rad = ang*m.pi/180
si=m.sin(ang_rad)
print("The sine of {} is {}".format(ang, si))



number_1=float( input("enter a number : "))
number_2=float(input("enter a second number : "))
addition=number_1+number_2
multiplication=number_1*number_2
print("the sum of {} and {} is {}".format(number_1,number_2,addition))
print("the product of {} and {} is {}".format(number_1,number_2,multiplication))



lenght=float(input("Enter the lenght : "))
print("The area of the cube is {}  and the volume is {}".format(lenght**2,lenght**3))


#total de billet

nb_10=float(input("Entrer le nombre de 10 : "))
nb_20=float(input("Entrer le nombre de 20 : "))
nb_50=float(input("Entrer le nombre de 50 : "))
total=nb_10*10+nb_20*20+nb_50*50
print("the total is {}".format(total))




#
side_1=float(input("side 1 : "))
side_2=float(input("side_2 : "))
angle=float(input("angle in degree : "))
angle=m.radians(angle)
c=m.sqrt(side_1**2+side_2**2 - 2*side_1*side_2*m.cos(angle))
print("given a triangle of sides {} and {} and an angle of {} between them, the third side is {}".format(side_1,side_2,angle,c**2))



message ='good morning'
print(message)
print(len(message))
print(message[0:2])
print(message.upper())
print(message.count('g'))
print(message.find('o'))
print(dir(message))





num=int(input("Enter the number : "))
if num%2==0:
    print("The number {} is even number".format(num))
else:
    print(f"the number {num} is odd")
    
    
    
    
    
H=float(input("enter your body height : "))
P=float(input("enter your weight : "))
BM=P/H**2
print(BM)
if BM<18.5:
    print("underweight")
elif BM>=18.5 and BM<25:
    print("normal weight")
elif BM>=25 and BM<30:
    print("overweight")
else:
    print("obesity")
    
    
    
num_1=float(input("enter your first number : "))
num_2=float(input("enter your second number : "))

if num_1>num_2:
    print(f"min is {num_2}")
elif num_1<num_2:
    print(f"min is {num_1}")
else :
    print("The number are equal")
    
    
    
    
num=int(input("Enter an integer value : "))
    
while num>0:
   res=num//3
   print(f"the integer division of {num} by 3 gives : {res}")
   num=int(input("Enter an integer value"))
print("We're done")





num=int(input("Enter an integer value : "))
ndiv=0 



while num>0 :
    res=num//3
    print("The integer division of {} by 3 gives : {}".format(num,res))
    ndiv=ndiv+1
    print("Number of division so far : {}".format(ndiv))
    num=int(input"Enter an integer value : "))
    
print("We're done")
print("total number of iterations : {}".format)





num=1
ndiv=0

while num>0 and num<211:
    if num%3==0:
        print(f"the number is {num}")
        ndiv=ndiv+1#Increase the value of the divisor counter made a unit
    num=num+1
    
print("total number of iterations : {}".format(ndiv))
print("We're done")




num=1
sum=0
while num<=10:
    sum=sum+num
    num=num+1
print(f"the sum of the 10 first is {sum}")



num=1
sum=0
while num<=10:
    sai=int(input("enter a number"))
    num=num+1
    sum=sum+sai
print(f"the average is {sum/10}")




for i in list(range (1,30)):
    print(i*"*")
    
j=1
while j<=4:
    print ("*"*j)
    j=j+1
    
    
   



i=int(input("enter a number : "))
product=1


while i>0:
    
    product=product*i
    i=i-1
    
print (product)
    
    
    



name='Jesaa29Roy'
size=len(name)
i=0
while i<size:
    if name[i].isdecimal():
        break;
        print(name[i])
    print(name[i],end=' ')
    i=i+1
print("\nThe execution has stopped")
        


#week3
n=int(input("Enter the value of n :"))
for i in range (1,n+1,2):
    q_i=i**2
    print(q_i)


#accumulator becarful start with 1!=0
sum=0
for i in range(6):
    sum=sum+1
    print(f"the value of sum is in each iteration : {sum}")
print(f"The sum is valid {sum}")

prod=1
for  i in range (1,6):
    prod=prod*i
    print(f"the partial sum is {prod}")

#exo1
sum=1
val=int(input("Enter a value : "))
for i in range (0,val+1):
    sum=sum+i
print(sum)
    
#exo2
sum=0
val=int(input("Enter a value: "))
for i in range(1,val+1):
    sum=sum+(i+1)/i**2
print(f"the sum is {sum}")

#exo4

for i in range(1,10):
    for j in range(1,10) :
        print(f"{i}{j}")
        

#exo5

for i in range(1,10):
    for j in range(1,10) :
        if(i!=j):
            print(f"{i}{j}")

            
#exo 6

a=int(input("Enter the number of triangular numbers you want : "))
for i in range(0,a+1) :
    t=i*(i+1)/2
    print(t)
    

#exo 7

for i in range(0,10):
    for j in range(0,10) :
        for k in range(0,10) :
            print(f"{i}{j}{k}")
            
            

#exo8


for i in range(0,10):
    for j in range(0,10) :
        for k in range(0,10) :
            if(i+j+k==22):
                print(f"{i}{j}{k}")

         


for i in range (0,10):
    for j in range(0,10) :
        for k in range (0,10) : 
            if (i**3+j**3+k**3 == (i*100+j*10+k)):
                print(f"{i}{j}{k}")
                


n=int(input("Rentre une valeur :"))
for i in range (1,n+1):
    if n%i==0 :
        print (i)
            


num=int(input("Enter a positive number"))
sum=0
for i in range (0,num+1):
    odd_number =2*i+1
    print(f"the number is odd")
    sum=sum+odd_number
print(f"the sum of the first {num}odd numbers is {sum}")

#exo 9

a=1
b=1


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
    thelist.append(1/i):
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
    
    
    



#creating dictionary


country_capitals={"United states":"Washington DC","Italy":"Rome","England":"London"}
print(country_capitals)





my_dict={1:"Hello",(1,2):"Hello Hi",3:[1,2,3]}
print(my_dict)
print(len(my_dict))


Dict={1:"GEEKS",2:"for",3:{'A':"Welcome",'B':'to','C':"Geeks"}}
print(Dict[3]['A'])
Dict[1]="SUUUUU"

print(Dict)


#rajouter un element 


Dict[4]="gekk"
print(Dict)
#remove

del Dict[4]
print(Dict)





my_list{1:"Hello", 2:"Howdy"}

print(1 in my list)#true

print("Howdy"  not in my_list)#false
print("Hello" in my_list)#false


for keys, values in Dict.items():
    print(country_capitals.keys())
    
    

dict1={1:"Python",2:"Java",3:"Ruby",4:"Scala"}

print(dict1.keys())
dict1.pop(4)
print(dict1)
dict1.popitem()
print(dict1)
dict1.update({3:"Scala"})
print(dict1)


#create a sequence of strings
cities =('Paris','Athens','Madrid')
country=('France','Grece','Spain')


continent='Europe'

my_dictionnary=dict.fromkeys(cities,country)
print(my_dictionnary)

    
    #exo 1
keys=['Ten','Twenty','Thirty']
values=[10,20,30]
my_dic=dict.fromkeys(keys,values)
    
print(my_dic)

res_dict=dict(zip(keys,values))
print(res_dict)


#exo 2

dict1={"ten":10,"twenty":20,"thirty":30}
dict2={"thirty":30,"fourty":40, "fifty":50}

dict1.update(dict2)
print(dict1)


#exo 3

employees=['Kelly','Emma']
defaults={"designation":"Developer","salary":8000}
my_dic=dict.fromkeys(employees,defaults)
print(my_dic)




#exo4

sample_dict={
    "name":"Kelly",
    "age":25,
    "salary":8000,
    "city":"New York"}

sample_dict.pop("name")
sample_dict.pop("salary")



print(sample_dict)


#exo 5

sample_dict={'a':100,'b':200,'c':300}
if 200 in sample_dict.values():
    print('200 present in a dict')
    
    

#exo 6

sample_dict={
    'emp1':{'name':'John','salary': 7500},
    'emp2':{'name':'Emma','salary':8000},
    'emp3':{'name':'Brad','salary':500}}

sample_dict.update['emp3']['salary']=8500



#probleme 1

def element(dic):
    ele=input("Enter the symbol of the element : ")
    temp=float(input("Enter the temperature of the element : "))
    
    for symbol in dic:
        if ele==symbol:
            if temp<dic[ele]['Melting point']:
                print("The element is solid")
            elif temp>dic[ele]['Boiling point']:
                print("The element is gaz")
            else :
                print("The element is liquid")



dic={'H':{'atomic number':'1','Melting point':14,'Boiling point':20},
     'He':{'atomic number':'2','Melting point':1,'Boiling point':4},
     'Li':{'atomic number':'3','Melting point':453,'Boiling point':1603},
     'Be':{'atomic number':'4','Melting point':1560,'Boiling point':2742},
     'B':{'atomic number':'5','Melting point':2349,'Boiling point':4200},
     'C':{'atomic number':'6','Melting point':3915,'Boiling point':3915},
     'N':{'atomic number':'7','Melting point':63,'Boiling point':77},
     'O':{'atomic number':'8','Melting point':54,'Boiling point':90},
     'F':{'atomic number':'9','Melting point':53,'Boiling point':85},
     'Ne':{'atomic number':'10','Melting point':25,'Boiling point':27}
     }


element(dic)
            
#probleme 2
    

bank={'ANZ':{'Y1-2':2.3,'Y3':4.1},
      'Bank of Australia':{'Y1-2':0.1,'Y3':5},
      'CommonwealthBank':{'Y1-2':3.5,'Y3':3.8},
      'Westpac':{'Y1-2':3.7,'Y3':3.7}}
bk=input("print the name of your bank : ")
mortage=float(input("print the value of the mortage : "))
years=float(input("Enter the number of year : "))
if (years<=2):
    mortage =mortage + bank[bk]["Y1-2"]*(1/12)
    print(mortage)
else:
    mortage= mortage+bank[bk]["Y3"]*(1/12)
    print(mortage)
    




def myfunction(child3,child2,child1):
    print("the youngest"+child3)


myfunction(child1="Emil",child2="Tobias",child3="suuu")


def my_function(**kid):
    print("his last name "+kid["lname"])
    
my_function(fname="Tobias",lname="Refnes")








def maxnumbers(num1,num2):
    if (num1>num2):
        print(num1)
    else:
        print(num2)
        


a=float(input("enter a number : "))
b=float(input("enter a second number : "))
maxnumbers(a,b)



def minmax(*args):
    args=list(args)
    args.sort()
    print(args[0])
    print(args[len(args)-1])
    
        
   

minmax(3,6,8,2,1)
    
    
    

while True:
    try:
        num = int(input("Enter a number : "))
    
    except ValueError as e:
        if num < 0:
            print("Rentrer un nombre positif")
        elif isinstance(num,float):
            print("pas de float que des int")
        
            
         
    else:  
        
        if(num%2)==0:
            print("{0} is Even".format(num))
            break
        else:
            print("{0} is Odd".format(num))
            break
        

        
        
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

import numpy
npoints=21
values=numpy.linspace(10,30,npoints)
values[6]=1
print(values)
 '''
