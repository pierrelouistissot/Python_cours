# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 00:14:38 2023

@author: tisso
"""

import numpy as np

#exercice 1

angstrom_values=np.linspace(1.0,5.0,21)
angstrom_values=angstrom_values*0.1
print(angstrom_values)

#exercice 2

X0=float(input("Enter the X0 value : "))
S=float(input("Enter the S value : "))
Xi=float(input("Enter the initial value of X : "))
Xf=float(input("Enter the final value of X : "))
Point=int(input("Enter the number of point the table must have : "))
x_array=np.linspace(Xi,Xf,Point)
y_array=(1/np.sqrt(2*np.pi))*np.exp(-0.5*((x_array-X0)/S)**2)#the function
print("x       y")
for x, y in zip(x_array, y_array):
    print(f"{x:.3f}   {y:.5f}")
    
    

#exercice 3

temp_mar = [13.8, 13.3, 13.9, 15.0, 16.4, 20.0, 21.9, 22.3, 22.0, 21.2, 18.8, 16.0]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
'November', 'December']
#changing in numpy array
temp_mar_array=np.array(temp_mar)

#mean
print(np.mean(temp_mar_array))
#min
month_index_min=np.argmin(temp_mar_array)
print(f"{temp_mar[month_index_min]},{months[month_index_min]}")
#max
month_index_max=np.argmax(temp_mar_array)
print(f"{temp_mar[month_index_max]},{months[month_index_max]}")


#exerice 4

 
number_student=int(input("Enter the number of students who have taken an exam : "))

theory_marks=[]
problem_marks=[]

for i in range (number_student):
    
    while True:
        theory_mark=float(input(f"Enter the theory mark for student {i + 1} : "))   
        if(theory_mark > 10 or theory_mark < 0):#if the grade is not between (0-10)
            print("the grade as to be between 0 and 10")
        else:
            break
    
    while True:
        problem_mark=float(input(f"Enter the problem mark for student {i + 1} : "))
        if(problem_mark > 10 or problem_mark < 0):
            print("the grade as to be between 0 and 10")
        else:
            break

    theory_marks.append(theory_mark)
    problem_marks.append(problem_mark)
    
    total_marks=[0.4*theory_mark +0.6*problem_mark for theory_mark,problem_mark in zip(theory_marks,problem_marks)] #creating the total marks array
    
print("\nStudent   Theory   Problem   Total")
for i,(theory_mark,problem_mark,total_mark)in enumerate(zip(theory_marks, problem_marks, total_marks)):
    print(f'   {i}       {theory_mark}       {problem_mark}       {total_mark}')
    
    

print(f"The maximal total grade :{ np.max(total_marks)}")
print(f"The minimal total grade :{ np.min(total_marks)}")
print(f"The average total grade :{ np.mean(total_marks)}")
print(f"The position index of the max grade :{ np.argmax(total_marks)}")


    
    
    
    
        
    
    




