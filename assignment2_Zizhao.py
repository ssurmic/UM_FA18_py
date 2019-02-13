#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
Created on Tue Oct  2 19:17:44 2018

@author: zizhaozhang
@umid:   35009521
""" 

# =============================================================================
# relevant packages and module
# =============================================================================
import math
import collections
from statistics import mean 
import numpy as np
import matplotlib.pyplot as plt
#define a function to remove duplicates in list while keeping order============

def unique_list(lists):
    """ 
        input: 
            lists: list
    
        output: 
            lists: list
    """
    unique_set = set()
    return [x for x in lists if not (x in unique_set or unique_set.add(x))]


#define a function to count the ips within each minute in order according to the 
#time list generate above======================================================

def count_IP(main_list,time_reference,index):
    """ 
        input: 
            main_list: list
            time_reference: list
            index: int
    
        output:
            len(ip_set):int
            
    """
    ip_set = set()
    for sub_lists in main_list:
        if sub_lists[0] == time_reference[index]:
            for j in range(1,3):
                ip_set.add(sub_lists[j])
    return len(ip_set)



#function of calculating the percentile using left and right pointer===========

def percentile_of_list(number_list, percent):
    """ 
        input: 
            number_list: list
            percent: int
    
        output: 
            left_half+right_half: float
    """
    if not number_list or len(number_list) == 0:
        return None
    #calculate the index of the desired value
    index = (len(number_list)-1) * (percent/100)
    #upper and lower bounds
    floor = math.floor(index)
    ceiling = math.ceil(index)
    if floor == ceiling:
        return (number_list[int(index)])
    left_half = number_list[int(floor)] * (ceiling-index)
    right_half = number_list[int(ceiling)] * (index-floor)
    return left_half+right_half


#define a fuction counts occuance of distinct ips within minute timestamp======
def IP_occurance(main_list,reference_list,index):
    """ 
        input: 
            main_list: list
            reference_list: list
            index: int
    
        output: 
            collections.Counter(temp).items(): collection
    """
    temp = []
    for x in main_list:
        if x[0] == reference_list[index]:
            temp.append(x[1])
            temp.append(x[2])                
    return collections.Counter(temp).items()
#calculate the mean of each occurance within minute============================
def mean_occurance(main_list,reference_list):
    """ 
        input: 
            main_list: list
            reference_list: list
    
        output: 
            mean_list: list
    """
    mean_list = []
    for i in range(len(reference_list)):
        ip_occur = list(IP_occurance(main_list,reference_list,i))
        occurance = [item[1] for item in ip_occur]
        mean_list.append(mean(occurance))
    return mean_list


def question2(data_set):
    """ 
        input: 
            data_set: numpy.ndarray
    
        output: 
            total_side_affects: numpy.ndarray
    """
    incidents_count = data_set.sum(axis = 0)[1:]
    incidents_cat = ['Serious','Death','Non-serious']
    total_side_affects = np.column_stack((incidents_cat,incidents_count))
    return total_side_affects

def question3(data_set):
    """ 
        input: 
            data_set: numpy.ndarray
    
        output: 
            numpy.ndarray
    """
    side_affects_by_year = np.sum(np.delete(data_set, 0, axis=1),axis=1)
    return np.column_stack((data_set[:,0],side_affects_by_year))


def question4(data_set):
    """ 
        input: 
            data_set: numpy.ndarray
    
        output: 
            numpy.ndarray
    """
    highest_year = data_set[data_set.argmax(axis = 0)[1:]][:,0]
    return np.column_stack((['Serious','Death','Non-serious'],highest_year))

def question5(data_set):
    """ 
        input: 
            data_set: numpy.ndarray
    
        output: 
            numpy.ndarray
    """
    #highest_indicent_by_year
    incident_array = np.delete(data_set, 0, axis=1)
    highest_incident = np.argmax(incident_array,axis = 1)
    incident_dict = {0:'Serious', 1:'Death', 2:'Non-serious'}
    highest_incident1 = np.vectorize(incident_dict.get)(highest_incident)
    return np.column_stack((data_set[:,0],highest_incident1))

def question6(data_set):
    """ 
        input: 
            data_set: numpy.ndarray
    
        output: 
            bi-dimensional numpy.ndarray
    """
    incident = data_set[:,1:4].sum(axis=1)
    normalized_rate = data_set[:,1:4][np.newaxis,:] / \
    (incident[:,np.newaxis]).astype(int)
    return normalized_rate



def question7(data_set):
    """ 
        input: 
            data_set: numpy.ndarray
    
        output: 
            plot: NoneType
    """
    incident = ["serious ", "seath", "son-serious"]
    plt.stackplot(data_set[:,0], data_set[:,1], data_set[:,2],\
                  data_set[:,3], labels=incident)
    plt.xlabel('Year')
    plt.ylabel('incident_count')
    plt.legend(loc='upper left')
    plt.show()














