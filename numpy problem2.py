# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:06:33 2023

@author: tisso
"""
import numpy as np
import matplotlib.pyplot as plt



#exo
def exo1():
    vector=np.linspace(0,20,21)
    vector[9,16]=-vector[9,16]
    print(vector)

#exo 2

def exo2():
    vector=np.linspace(15,55,41)
    print(vector[1:-1])


#exo 3
def exo3():
    array=np.zeros((3,4))
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            val=float(input(f"entrer la valeur de la case [{i},{j}] : "))
            array[i,j]=val
    print(array)



#exo 4
def exo4():
    vector=np.linspace(5,50,10)
    print(vector)



#exo 5
def exo5():
    vect=np.zeros(5)
    for i in range(len(vect)):
        vect[i]=np.random.randint(0,10)
    print(vect)


#exo 6
def exo6():

    size_1=int(input("Entrer la taille du premier vecteur : "))
    vector1=np.zeros(size_1)
    x=True
    while x:
        size_2=int(input("Entrer la taille du 2ieme vecteur : "))
        if size_2!=size_1:
            print("same size pls!")
        else:
            x=False
    vector2=np.zeros(size_2)
    
        
    for i in range(len(vector1)):
        value=int(input(f"enter the {i} value of vector 1 : "))
        vector1[i]=value
    for i in range(len(vector2)):
        value=int(input(f"enter the {i} value of vector 2 : "))
        vector2[i]=value
    
    result=vector1*vector2
    print(result)



#exo 7
def exo7():
    vecteur=np.linspace(10,21,12).reshape(3,4)
    print(vecteur)



#exo 8
def exo8():
    #creating the matrix
    row=int(input("Enter the number of row : "))
    column=int(input("Enter the number of column : "))
    vector=np.zeros((row,column))
    for i in range(row):
        for j in range(column):
            vector[i,j]=np.random.randint(1,10)
    print(vector)
    #size
    print(f"number of row :{vector.shape[0]}")
    print(f"number of column :{vector.shape[1]}")


#exo 9
def exo9():
    
    matrix=np.zeros((4,4))
    matrix[1::2, ::2] = 1
    matrix[::2, 1::2] = 1
    print(matrix)
    


#exo 10
def exo10():
    array1=[0,10,20,40,60]
    array2=[10,30,40]
    common_values = np.intersect1d(array1, array2)
    print(common_values)
    
    commonvalue=[]
    for i in range (len(array2)):
        for j in range(len(array1)):
            if(array2[i]==array1[j]):
                commonvalue.append(array2[i])
    print(commonvalue)


#exo 11

def exo11():

    array=[10,10,20,20,30,30]
    unique_elements = np.unique(array)
    print(unique_elements)
    
    original_array_2d = np.array([[1, 1], [2, 3]])
    unique_elements_2d = np.unique(original_array_2d)
    print(unique_elements_2d)



#exo 12
def exo12():
    
    size_1=int(input("Entrer la taille du premier vecteur : "))
    vector1=np.zeros(size_1)
    x=True
    while x:
        size_2=int(input("Entrer la taille du 2ieme vecteur : "))
        if size_2!=size_1:
            print("same size pls!")
        else:
            x=False
    vector2=np.zeros(size_2)
    
        
    for i in range(len(vector1)):
        value=int(input(f"enter the {i} value of vector 1 : "))
        vector1[i]=value
    for i in range(len(vector2)):
        value=int(input(f"enter the {i} value of vector 2 : "))
        vector2[i]=value
    
    cross_product=np.cross(vector1,vector2)
    print(cross_product)
    



#exo 13
def exo13():

    cartesian_coordinates = np.random.rand(10, 2)
    print(f'Here are the cartesian coordinates : {cartesian_coordinates}')
    x = cartesian_coordinates[:, 0]#take the x axis values
    y = cartesian_coordinates[:, 1]#take the y
    
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    print(f'Here are your polar coordinates after the transformation : r={r} \n theta={theta}')



#exo 14

def exo14():
    
    original_array = list(range(100)) 
    n=float(input("Enter the value you want to compare :" )) 
    
    
    closest_index=0
    min_difference = float(100)
    
    
    for index, value in enumerate(original_array):
        
        difference = abs(value - n)
        if difference < min_difference:
            min_difference = difference  
            closest_index = index
    
    
    closest_value = original_array[closest_index]
    print(closest_value)




exercises = {
    1: exo1,
    2: exo2,
    3: exo3,
    4: exo4,
    5: exo5,
    6: exo6,
    7: exo7,
    8: exo8,
    9: exo9,
    10: exo10,
    11: exo11,
    12: exo12,
    13: exo13,
    14: exo14
}
while True:
    try:
        exercise_number = input("enter the exercice you want to try (1-14), or press enter to Quit : ")
        
        if exercise_number == '':
            break  
        
        exercise_number = int(exercise_number)
        
        if 1 <= exercise_number <= 14:
            exercises[exercise_number]()
        else:
            print("Numéro d'exercice non valide. Veuillez entrer un numéro entre 1 et 14.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")