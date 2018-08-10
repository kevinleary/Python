# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 15:35:35 2018

@author: Kev-PC
"""


def find_dup_str(s, n):
    #find the first letter in the string then compare to the others
    og_string = ''
    dup_string = ''
    
    for i in list(range(len(s))):        #iterate through string
        og_string = s[i:i+n:1]
        #j = n+i                            #alwasy starts right after og_string
        if(len(s[i:i+n:1]) < n):            #case for if the string is less then n
            return ""     

        for j in list(range(n+i, len(s))):
            dup_string = s[j:j+n:1]
            #print(s[j:j+n:1])
           
            if(og_string == dup_string):
                return og_string
        
        if(len(og_string) != len(dup_string)):      # when it stops being same len stop comparing
                return ""

        if(og_string == dup_string):
                return og_string
                   
        
        if(og_string != dup_string and i == (len(s) - 1)):
            return ""
            

def find_max_dup(s):
    
    i = int(len(s) - 1)         #i starts at second element as it becomes n
    
    while(i > 0):       #increment through
        
        
        if(find_dup_str(s, i) != ""):
            break
        
        i = i-1
    
    return find_dup_str(s, i)

s = input("Enter a string to find dups: ")
#n = int(input("Enter the length of duplicate: "))

#print(find_dup_str(s,n))
print(find_max_dup(s))
