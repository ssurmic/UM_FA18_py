#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:14:15 2018

@author: zizhaozhang
@umid: 35009521
"""

# =============================================================================
# relevant packages
# =============================================================================
import numpy as np
# =============================================================================
# Question 2.1:
# =============================================================================
fda_data = np.loadtxt('/Users/zizhaozhang/Desktop/umich/607/hw2/adverseCountsFinal.txt')
# =============================================================================
# Question 2.2:
# =============================================================================
def question2(data_set):
    incidents_count = data_set.sum(axis = 0)[1:]
    incidents_cat = ['Serious','Death','Non-serious']
    total_side_affects = np.column_stack((incidents_cat,incidents_count))
    return total_side_affects
question2(fda_data)
# =============================================================================
# Question 2.3:
# =============================================================================
def question3(data_set):
    side_affects_by_year = np.sum(np.delete(data_set, 0, axis=1),axis=1)
    return np.column_stack((data_set[:,0],side_affects_by_year))

# =============================================================================
# Question 2.4:
# =============================================================================
def question4(data_set):
    highest_year = data_set[data_set.argmax(axis = 0)[1:]][:,0]
    return np.column_stack((['Serious','Death','Non-serious'],highest_year))
# =============================================================================
# Question 2.5:
# =============================================================================
def question5(data_set):
    #highest_indicent_by_year
    incident_array = np.delete(data_set, 0, axis=1)
    highest_incident = np.argmax(incident_array,axis = 1)
    incident_dict = {0:'Serious', 1:'Death', 2:'Non-serious'}
    highest_incident1 = np.vectorize(incident_dict.get)(highest_incident)
    return np.column_stack((data_set[:,0],highest_incident1))
# =============================================================================
# Question 2.6:
# =============================================================================
def question6(data_set):
    incident = data_set[:,1:4].sum(axis=1)
    normalized_rate = data_set[:,1:4][np.newaxis,:] / \
    (incident[:,np.newaxis]).astype(int)
    return np.column_stack((data_set[:,0].astype(int),normalized_rate[0]))
# =============================================================================
# Question 2.7:
# =============================================================================
import matplotlib.pyplot as plt

def question7(data_set):
    incident = ["serious ", "seath", "son-serious"]
    plt.stackplot(data_set[:,0], data_set[:,1], data_set[:,2],\
                  data_set[:,3], labels=incident)
    plt.xlabel('Year')
    plt.ylabel('incident_count')
    plt.legend(loc='upper left')
    plt.show()