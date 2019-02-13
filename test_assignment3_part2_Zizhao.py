#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:10:34 2018

@author: zizhaozhang
@UMID: 35009521

"""


# =============================================================================
# relevant packages and module
# =============================================================================
import pandas as pd
import random
import numpy as np
# =============================================================================
# Question 2.1
# =============================================================================
#setting up the months list of desired length
months_list = [["January"]*31,["February"]*28,["March"]*31,["April"]*30, \
 ["May"]*31,["June"]*30,["July"]*31,["August"]*31, \
 ["September"]*30,["October"]*31,["November"]*30, ["December"]*31]
month_list_flat = [item for sublist in months_list for item in sublist]
#setting up the days list of desired length
days_list = [list(range(1,31+1)),list(range(1,28+1)),list(range(1,31+1)), \
             list(range(1,30+1)),list(range(1,31+1)),list(range(1,30+1)), \
             list(range(1,31+1)),list(range(1,31+1)),list(range(1,30+1)), \
             list(range(1,31+1)),list(range(1,30+1)),list(range(1,31+1))]
days_list_flat = [item for sublist in days_list for item in sublist]
#setting up the days in week list of desired length
week_list = []
week_legend = ['Monday', 'Tuesday', \
               'Wednesday','Thursday', \
               'Friday', 'Saturday', \
                      'Sunday']
for index in list(range(0,365)):
    if (index+1)%7 == 1: 
        week_list.append(week_legend[0])
    elif (index+1)%7 == 2:
        week_list.append(week_legend[1])
    elif (index+1)%7 == 3:
        week_list.append(week_legend[2])
    elif (index+1)%7 == 4:
        week_list.append(week_legend[3])
    elif (index+1)%7 == 5:
        week_list.append(week_legend[4])
    elif (index+1)%7 == 6:
        week_list.append(week_legend[5])
    elif (index+1)%7 == 0:
        week_list.append(week_legend[6])
#setting up the values list with random vaule between 0:100(inclusive)
value_list = []
for i in range(365):
    value_list.append(random.randint(0,100))
#setting up the panda data frame
dailyValues1 = pd.DataFrame({ 'Year' : [2018]*365,\
                    'Month': month_list_flat, \
                    'Day' : days_list_flat, \
                    'Weekday': week_list, \
                    'Value' : value_list })
# =============================================================================
# Question 2.2
# =============================================================================
#denote a month_list_2 for reference in later steps
months_list_2 = ["January","February","March","April", \
                 "May","June","July","August", \
                 "September","October","November","December"]

dailyValues2 = pd.DataFrame(np.nan, index = months_list_2,\
                            columns = list(range(1,32)) )
#remapp the items in the dataframe accordingly
for item in months_list_2:
    days_in_month = dailyValues1.loc[dailyValues1.Month == item, "Value"]
    dailyValues2.loc[item,:np.size(days_in_month)] = np.array(days_in_month)
    
#delete the unessary variables for the ease of grading
del days_in_month, days_list, days_list_flat, i, index, item, month_list_flat,\
months_list, months_list_2, value_list, week_legend, week_list
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    