# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 16:16:00 2018

@author: Kev-PC
"""
#Part A
numbers = [4, -3, 0, 2, -1, 5]
numbers_squared = ['y*y=' + str(n*n) for n in numbers]
#print(numbers_squared)

#part B

numbers_solution = ['solution #' + str(n+1) + '=' + str(numbers[n]**2) for n in range(len(numbers))] 
print(numbers_solution)

#part C

lst = ["zero", "one", "two", "three"]

new_lst = [str(i) + ' ' + lst[i] for i in range(len(lst))]

print(new_lst)

#part D

a = ['a','b','c']
b = [1,2]
cartesian = []

for x, y in [(x,y) for x in a for y in b]:
    cartesian += (x,y)

print(cartesian)

#part E

lst1 = [56, 25, 8, 11, 16, 20, 18, 50, 7, 42]
lst2 = [5, 3, 6]

