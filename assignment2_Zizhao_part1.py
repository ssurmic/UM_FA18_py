#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
Created on Tue Oct  2 19:17:44 2018

@author: zizhaozhang
@umid:   35009521
"""

# =============================================================================
# relevant packages
# =============================================================================
import gzip
import shutil
import re
#import numpy as np
# =============================================================================
# Question 1.1:
# =============================================================================


#extract the compressed gz file into regular txt file
with gzip.open('/Users/zizhaozhang/Desktop/umich/607/hw2/maccdc2012_00016.txt.gz',\
               'rb') as f_in:
    with open('maccdc2012_00016.txt', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

#read in files, and split files by newline
#data cleaning within the txt file with regular expression
#difine pattern and use lambda function to find desired lines
text_file = open("./maccdc2012_00016.txt", "rt")
lines = text_file.read().split('\n')
ip_pattern = re.compile(r'([0-9:.]*) IP ([0-9.]*) > ([0-9.]*)\b')
ip_list = list(filter(lambda i: bool(ip_pattern.match(i)),lines))
#split as array of lists
new_ip_list = [ip_list[i:i+1] for i in range(0, len(ip_list), 1)]
#nested for loops to iterate within each list and find dates-ip-ip pattern items
dates_ips = []
for sub_list in new_ip_list:
    for items in sub_list:
        for i in range(1,4):
            dates_ips.append((ip_pattern.match(items).group(i)))
#final array of list stores ips and minutes for future use
final_ip_list = [dates_ips[i:i+3] for i in range(0, len(dates_ips), 3)]
#remove all the unnessacry time information====================================
for i in range(len(final_ip_list)):
    final_ip_list[i][0] = final_ip_list[i][0][0:5]

#define a function to remove duplicates in list while keeping order============
def unique_list(lists):
    unique_set = set()
    return [x for x in lists if not (x in unique_set or unique_set.add(x))]

#clean the time list in minutes and in order===================================
time_list = []
for x in final_ip_list:
    time_list.append(x[0])
time_list = unique_list(time_list)
#define a function to count the ips within each minute in order according to the 
#time list generate above======================================================
def count_IP(main_list,time_reference,index):
    ip_set = set()
    for sub_lists in main_list:
        if sub_lists[0] == time_reference[index]:
            for j in range(1,3):
                ip_set.add(sub_lists[j])
    return len(ip_set)
#initiate ip_count list, and call count_IP accordingly to the index of time_list
ip_counts = []
for i in range(0,len(time_list)):
    ip_counts.append(count_IP(final_ip_list,time_list,i))
#merge two list together with description to present the time and ip counts
final_list = ["time: " + m+ ';'+" ip count: "+ str(n) for m,n\
              in zip(time_list,ip_counts)]


# =============================================================================
# Question 1.2:
# =============================================================================
#before calculating the percentile, the list of ip_counts need to be sorted
ip_counts.sort()
#function of calculating the percentile using left and right pointer
import math
def percentile_of_list(number_list, percent):
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
#10 percentile :===============================================================
print('10th perentile of ip appearance: ',percentile_of_list(ip_counts,10))
#25 percentile :===============================================================
print('25th perentile of ip appearance: ',percentile_of_list(ip_counts,25))
#75 percentile :===============================================================
print('75th perentile of ip appearance: ',percentile_of_list(ip_counts,75))
#90 percentile :===============================================================
print('90th perentile of ip appearance: ',percentile_of_list(ip_counts,90))

# =============================================================================
# Question 1.3:
# =============================================================================
#import collections module to count the occurance into collection dataframe
import collections
#define a fuction counts occuance of distinct ips within minute timestamp
def IP_occurance(main_list,reference_list,index):
    temp = []
    for x in main_list:
        if x[0] == reference_list[index]:
            temp.append(x[1])
            temp.append(x[2])                
    return collections.Counter(temp).items()
#import statistics module to calculate the mean of each occurance within minute
from statistics import mean 
def mean_occurance(main_list,reference_list):
    mean_list = []
    for i in range(len(reference_list)):
        ip_occur = list(IP_occurance(main_list,reference_list,i))
        occurance = [item[1] for item in ip_occur]
        mean_list.append(mean(occurance))
    return mean_list
#format the final answer into a readable list
occurance_list = ["time: " + m+ ';'+" average ip occurance: "+ str(n) for m,n\
                  in zip(time_list,mean_occurance(final_ip_list,time_list))]

# =============================================================================
# Question 1.4:
# =============================================================================
#sort the mean occurance list before calculating the percentiles within timestamp
sort_mean = mean_occurance(final_ip_list,time_list)
sort_mean.sort()

#10 percentile :===============================================================
print('10th perentile of mean occurance: ', percentile_of_list(sort_mean,10))
#25 percentile :===============================================================
print('25th perentile of mean occurance: ',percentile_of_list(sort_mean,25))
#75 percentile :===============================================================
print('75th perentile of mean occurance: ',percentile_of_list(sort_mean,75))
#90 percentile :===============================================================
print('90th perentile of mean occurance: ',percentile_of_list(sort_mean,90))


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














