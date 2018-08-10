# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 00:46:58 2018

@author: Kev-PC
"""
limit=int(input("Enter upper limit: "))
c=0
n=2
while(c<limit):     #as long as C is lower then the limit
    for m in range(1,n+1):
        a=n*n - m*m
        b=2*n*m
        c=n*n+m*m
        if(c>limit):    #goes til limit
            break
        if(a==0 or b==0 or c==0):       #wont display a 0
            break
        if((a%3 == 0 and b%4==0 and c%5 == 0) or (a%4 == 0 and b%3 == 0 and c%5 == 0)):   #wont duplicate a primitive triple
            break
        print(a,b,c)
    n=n+1

x = 1
c = 0
while(c<limit):     #for primitive triples
    
    a = x*3
    b = x*4
    c = x*5
    
    print(a,b,c)
    
    x = x+1