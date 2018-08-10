# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 14:33:40 2018

@author: Kev-PC
"""

import pylab



fun_str = input("Enter function with variable x: ")
ns = int(input("Enter the number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))

xrange = (xmax - xmin) / ns
x = xmin
i = 0

xs = list()
ys = list()

while(x <= xmax):
    xs.append(x)
    x += xrange
    
for x in xs:
    y = eval(fun_str)
    ys.append(y)

print("          X             Y")
print("-------------------------")
while(i < 20):
    
    print("         {0}          {1}".format(xs[i], ys[i]))
    i= i+1;
    
print("--------------------------")
print("More values hidden")
    
pylab.plot(xs,ys, "bo-")

pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title(fun_str)