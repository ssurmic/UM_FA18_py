#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:27:59 2018

@author: zizhaozhang
"""
# =============================================================================
# relevant packages and module
# =============================================================================
import gzip
import shutil
import re
import assignment2_Zizhao as test
import math
import collections

# =============================================================================
# Question1.1
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

#clean the time list in minutes and in order===================================
time_list = []
for x in final_ip_list:
    time_list.append(x[0])
time_list = test.unique_list(time_list)
#initiate ip_count list, and call count_IP accordingly to the index of time_list
ip_counts = []
for i in range(0,len(time_list)):
    ip_counts.append(test.count_IP(final_ip_list,time_list,i))
#merge two list together with description to present the time and ip counts
final_list = ["time: " + m+ ';'+" ip count: "+ str(n) for m,n\
              in zip(time_list,ip_counts)]
#print out the final result to 1.1
print(final_list)
# =============================================================================
# Question 1.2:
# =============================================================================
#before calculating the percentile, the list of ip_counts need to be sorted
ip_counts.sort()
#10 percentile :===============================================================
print('10th perentile of ip appearance:',test.percentile_of_list(ip_counts,10))
#25 percentile :===============================================================
print('25th perentile of ip appearance:',test.percentile_of_list(ip_counts,25))
#75 percentile :===============================================================
print('75th perentile of ip appearance:',test.percentile_of_list(ip_counts,75))
#90 percentile :===============================================================
print('90th perentile of ip appearance:',test.percentile_of_list(ip_counts,90))
# =============================================================================
# Question 1.3:
# =============================================================================
occurance_list = ["time: " + m+ ';'+" average ip occurance: "+ str(n) for m,n\
                  in zip(time_list,test.mean_occurance(final_ip_list,time_list\
                                                       ))]
print(occurance_list) 
# =============================================================================
# Question 1.4:
# =============================================================================
#sort the mean occurance list before calculating the percentiles
sort_mean = test.mean_occurance(final_ip_list,time_list)
sort_mean.sort()  
#10 percentile :===============================================================
print('10th perentile of occurance: ',test.percentile_of_list(sort_mean,10))
#25 percentile :===============================================================
print('25th perentile of occurance: ',test.percentile_of_list(sort_mean,25))
#75 percentile :===============================================================
print('75th perentile of occurance: ',test.percentile_of_list(sort_mean,75))
#90 percentile :===============================================================
print('90th perentile of occurance: ',test.percentile_of_list(sort_mean,90))                









































