# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("This program determines the weekly salary for an employee.",
      "\nThe salary is the sum of the hourly rate times the",
      "hours worked, plus the bonus.",     
      "\nFor work hours exceeding 40 per week, an overtime rate",
      "of 1.5 is applied.",
      "\nThe user must indicate if the worker has received a",
      "bonus by answering a y/n question.",
      "\nInput consists of: hours worked, hourly rate, bonus."
      "\nThe output is the total salary for this week.")

hours_str = input("Enter the number of hours worked this week: " )
hours_float = int(hours_str)
salary_str = input("Enter the salary rate per hour (do not include the '$' sign):")
salary_float = int(salary_str)


if hours_float > 40:
    hours_ot_float = hours_float - 40
    overtime = (hours_ot_float * (salary_float *1.5))
    total = overtime + (40 * salary_float)
else:
    total = hours_float * salary_float
    overtime = 0.00
    
bonus_bool = input("Did the worker get a bonus ? (y/n): ")

if bonus_bool.lower() == 'y':
    bonus_str = input("Enter bonus: ")
    bonus_float = float(bonus_str)
    total = total + bonus_float
    
print("The total salary is $", total, " (overtime pay is $", overtime, ")")
    