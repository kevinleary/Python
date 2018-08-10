# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 15:17:48 2018

@author: Kev-PC
"""
#part A

def input_tuple(prompt, types, sep):
    
    try:
        new_tuple = tuple()
        info = input(prompt)            #setting up user given info
        info_extra = info.split(sep)
        if len(info_extra) != len(types):
            return new_tuple        #returns empty tuple
        else:
            for i in range(len(types)):
                new = types[i](info_extra[i])
                new_tuple.append(new)
            new_tuple = tuple(new_tuple)
        return new_tuple
    
    except ValueError:
        print("Wrong parameters entered")
        return ()
    
#part B

def input_tuple_lc(prompt, types, sep):
    
    try:
        new_list=[]
        info = input(prompt)
        info_extra = info.split(sep)
        
        if len(info_extra) != len(types):
            return new_list             #returns empty list
        
        else:
            new_list=[types[i](info_extra[i]) for i in range(len(types))]         
            new_tuple=tuple(new_list)
        return new_tuple
    
    except ValueError:
        print("Wrong parameters entered")
        return ()
    
#part C

def read_tuple(file_obj, types, sep):       #extra
    
    try:
        new_list=[]
        new_list=[types[i](file_obj[i]) for i in range(len(types))]     #reading from the file
        new_tuple=tuple(new_list)
        return new_tuple 
    
    except ValueError:
        print("Wrong parameters entered")
        return ()
    
call1 = input_tuple("Enter first name, last name, age (float), ID (int), fulltime (bool): ", (str, str, float, int, bool), ',')
call2 = input_tuple("Enter first name, last name, age (float), ID (int), fulltime (bool): ", (str, str, float, int, bool), ',')

f = open(“cars.csv”, “r”)

    for line in f:
        cars=read_tuple(line, (str, str, float, int, bool), ',')
        print(cars)