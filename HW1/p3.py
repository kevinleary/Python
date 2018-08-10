# -*- coding: utf-8 -*-
"""
Created on Mon May 21 21:17:28 2018

@author: Kev-PC
"""

while True:
    money = input("Enter amount: ")
    money = float(money)
    
    q = int(money / .25)
    qmoney_total = money - (q * .25)
    round(qmoney_total, 3)
    d = int((qmoney_total + .0001) / .10)
    dmoney_total = qmoney_total - (d * .10)
    
    p = int((dmoney_total + .0001) / .01)
    pmoney_total = dmoney_total - (p * .01)
    
    ct = int(q + d + p)
    
    print("$", money, "makes ", q, "quarters, ", d, "dimes ", "and ",  p, "pennies ")
    print("(", ct, " coins), total amount in coins: $", money)