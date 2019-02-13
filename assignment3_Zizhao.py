#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 03:22:54 2018

@author: zizhaozhang
@UMID: 35009521

"""
# =============================================================================
# relevant packages and module
# =============================================================================
import os, gzip,shutil

#extrate all the "gz" file within hw3 directory and output in the hw3 dir


#define myfloat function to filter the NAs missing value
def myfloat(x):
    """
    Input: string or character
    Output: float
    Description: This function cast the type of inputs as float
    
    """
    try:
        return float(x)
    except ValueError:
        return float('nan')

def get_list(year):
    """
    Input: int(2000,2005,2010)
    Output: list 
    Description: This function reads through all the according txt files and
    returns a long list with required info
    
    """

    dir_path = './'
    text_files = [f for f in os.listdir(dir_path)\
                  if os.path.isfile(os.path.join(dir_path, f))\
                  and f.endswith(str(year)[-2:] + ".txt")]
    container = []
    for file in text_files:
        file_path = dir_path + '/' + str(file) #fill in all files in the list
        f = open(file_path,'r')
        lines1 = (f.read().split('\n'))
        container.append(lines1)
    flat_list = [item for sublist in container for item in sublist]
    list_exp = [flat_list[i:i+1] for i in range(0, len(flat_list), 1)]  
    year_list = [item for sublist in list_exp for item in sublist]
    return (year_list)

def remove_empty(string_list):
    """
    Input: list
    Output: boolean 
    Description: This function serves as a filter for removing empty sublists
    
    """

    for item in string_list:
        return (len(item)!=0)
    
def condition_bridge(string_list):
    """
    Input: list
    Output: boolean 
    Description: This function serves as a filter for filtering the valid 
    bridges
    
    """

    return (myfloat(string_list[18]) == 1.0) and \
        (myfloat(string_list[222:228])/10 >= 6.1) and \
        (string_list[373] == 'Y') and \
        (string_list[199] in['1','4','5','6','7','8']) 
        
import math
def q1_condition(array_list):
    """
    Input: list
    Output: boolean 
    Description: This function serves as a filter for filtering structure num
    that is valid in the nested list
    
    """

    return (array_list[0] != 0) and (math.isnan(array_list[0]) == False)

def q4_condition(array_list):
    """
    Input: list
    Output: boolean
    Description: This function serves as a filter for filtering the increasing
    values
    
    """

    return (array_list[2] <= array_list[3])
def filt_nan(sub):
    """
    Input: list
    Output: boolean
    Description: This function serves as a filter for filtering the nans within
    sublists.
    
    """

    return (math.isnan(sub[1]) == False) and (math.isnan(sub[2]) == False)





