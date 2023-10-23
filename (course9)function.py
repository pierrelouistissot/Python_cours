# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:36:11 2023

@author: tisso
"""

def find_largest_and_smallest(numbers):
    if len(numbers) != 5:
        return "Please provide exactly 5 numbers."

    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest

# Example usage:
a=int(input("Enter a value:"))
b=int(input("Enter a value:"))
c=int(input("Enter a value:"))
d=int(input("Enter a value:"))
e=int(input("Enter a value:"))
numbers = [a, b, c, d, e]

largest, smallest = find_largest_and_smallest(numbers)
print(f"The largest number is {largest}")
print(f"The smallest number is {smallest}")
-----------------------------------------------------

def evenodd():
   num=int(input("Enter a number:"))

   if(num%2)==0:
       print("{0} is even".format(num))
   else:
       print("{0} is odd".format(num))

try:
    evenodd()
except:
    print("Something went wrong")
else: 
    print("Nothing went wrong")
finally:
    print("Finished")
