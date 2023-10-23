# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:36:11 2023

@author: tisso
"""

#import panda as pd
#import numpy as np

f_name=open("name.txt")
for name in f_name:
    if "a" in name:
        name=name.strip()
        print("Hello {}".format(name))
'''      
f=open("test.txt","r")#reading
f=open("test.txt","w")#writing
f=open("test.txt","a")#appending
f=open("test.txt","r+")#reading and writing
print(f.name)
print(f.mode)
f.close()





#reading a file by each line
with open("sentence.txt","r") as f:
    f_content=f.read()
    print(f_content)
    
#reading a file as a list
with open("sentence.txt","r") as f:
    f_content=f.readlines()
    print(f_content)

#print line by line
with open("sentence.txt","r")as f:
    f_content=f.readline()
    print(f_content)
    f_content=f.readline()
    print(f_content, end ='')

'''
#create a file  and write test
with open("test3.txt","w")as f:
    f.write("Test")
    
    
#writing

with open("test3.txt","w")as f:
    f.write("Hello world")
    f.seek(0)
    f.write("R")

#changing a file
with open("test3.txt","w")as f: 
     val='names'
     val1="10"
     val2="niamh"
     f.write(val+'\n'+val1+'\n'+val2)
     f.seek(0)
     f.write("Test")
     f.seek(6)
     f.write('z')
     
with open("sentence.txt","r") as rf:
    with open("sentence_copy","w")as wf:
        for line in rf:
            wf.write(line)
#image
with open("python.jpg","r") as rf:
    with open("python_copy.jpg","w")as wf:
        for line in rf:
            wf.write(line)
            

    