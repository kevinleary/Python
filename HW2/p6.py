# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 15:56:32 2018

@author: Kev-PC
"""

import pylab

#Part A

def get_csv_data(f, string_pos_lst, sep=","):
    
    lebron_lst = []
    
    f.readline()
    for line in f:          #iterate through
        line_list = line.split(sep)
        if(string_pos_lst in line_list):        #special str values entered
            lebron_tuple = (str(string_pos_lst))
            lebron_list.append(lebron_tuple)
    return lebron_lst

#part B
    
def get_columns(lebron_lst, cols_lst):
    
    col_data = []
    for column in cols_lst:
        try:
            index = lebron_lst[0].index(column)
            tmp_col_data = []
            for lbj in lebron_lst[1:]:      #iterate through list with a splice
                tmp_col_data.append(lbj[index]) 
            col_data.append(tmp_col_data)

        except ValueError:
            print("Wrong columns taken")
            pass                #keep it going
           
    return col_data

    
bb_file = open(“lb-james.csv”, “r”)     #error here for some reason
james_lst = get_csv_data(bb_file, [0, 2, 3, 4], “,”)
print(james_lst)

selected_cols_lst = get_columns(james_lst, ["Season","Age","PTS"])

selected_col_list = get_columns(james_list, ["Season", "3P%", "2P%", "FT%"])

x_axis = [int(x.split("-")[0]) for x in selected_col_list[0]]
y1 = selected_col_list[1]
y2 = selected_col_list[2]
y3 = selected_col_list[3]

pylab.plot(x_axis, y1, '-b', label="3-point precentage")
pylab.plot(x_axis, y2, '-r', label="2-point precentage")
pylab.plot(x_axis, y3, '-g', label="free throw precentage")

pylab.title("Lebron vs Time")
pylab.xticks(x_axis, x_axis)

pylab.xlabel("Year")
pylab.ylabel("Percentage")
pylab.ylim(0, 1.0)