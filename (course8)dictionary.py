# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:10:57 2023

@author: tisso
"""

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





my_list={1:"Hello", 2:"Howdy"}

print(1 in my_list)#true

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