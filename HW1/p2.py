# -*- coding: utf-8 -*-
"""
Created on Mon May 21 19:59:29 2018

@author: Kev-PC
"""

import math
import pylab
import numpy as np

while True:
   a = float(input("Enter a: "))
   b = float(input("Enter b: "))
   c = float(input("Enter c: "))
   
   if ((b**2) - (4*a*c)) < 0:
       print("\nno real solutions")
       
   elif ((b**2) - (4*a*c)) > 0:
       x1 = float((-b - math.sqrt(b**2 - 4*a*c)) / (2 * a))
       x2 = float((-b + math.sqrt(b**2 - 4*a*c)) / (2 * a))
       print("two solutions: x1=", x1, " x2=", x2)
       x = np.linspace(-5,5, 100)
       y = ((a*x*x) + (b*x) + c)
       pylab.plot(x,y)
       
   elif ((b**2) - (4*a*c)) == 0:
       d = float((-b + math.sqrt(b**2 - 4*a*c)) / (2 * a))
       print("one solution: ", d)
       
