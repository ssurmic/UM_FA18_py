#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thur Oct 18 12:10:04 2018
@author: zizhaozhang
@UMID: 35009521
"""
#
import os, gzip,shutil
import assignment3_Zizhao as test3
from collections import Counter
import statistics as stats
#make sure no other txt file are in the current directory
os.system("rm -rf ./*10.txt")
os.system("rm -rf ./*00.txt")
os.system("rm -rf ./*05.txt")
#set ups and unzips 
for path, dir_list, file_list in \
os.walk('./'):
    for file_name in file_list:
        if file_name.endswith("txt.gz"):
            with gzip.open(str(path)+'/'+str(file_name),'rb') as f_in:
                with open( str(file_name)[0:-3], 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
l00 = test3.get_list(2000)
l05 = test3.get_list(2005)
l10 = test3.get_list(2010)
#assign an empty list
L_temp = l00+l05+l10

l00 = list(filter(test3.remove_empty,test3.get_list(2000)))
list_00 = list(filter(test3.condition_bridge,l00))

l10 = list(filter(test3.remove_empty,test3.get_list(2010)))
list_10 = list(filter(test3.condition_bridge,l10))

l05 = list(filter(test3.remove_empty,test3.get_list(2005)))
list_05 = list(filter(test3.condition_bridge,l05))
#build L
L = list_00+list_05+list_10
for j in range(len(L)):
    L[j] = [test3.myfloat(L[j][3:18]), test3.myfloat(L[j][0:3]), \
     test3.myfloat(L[j][156:160]), test3.myfloat(L[j][361:365]), \
     test3.myfloat(L[j][222:228]), test3.myfloat(L[j][164:170])]
L1 = list(filter(test3.q1_condition,L))
# =============================================================================
# Question 1.1
# =============================================================================
state=[]
for i in range(len(L1)):
    state.append(L1[i][1])
stateWithMostBridges = Counter(state).most_common(1)[0][0]

# =============================================================================
# Question 1.2
# =============================================================================
avgLenBridges = {}
for elem in L1:
    if elem[1] not in avgLenBridges:
        avgLenBridges[elem[1]] = []
    avgLenBridges[elem[1]].append(elem[4:5])
for key in avgLenBridges:
    avgLenBridges[key] = [stats.mean(i) for i in zip(*avgLenBridges[key])][0]

# =============================================================================
# Question 1.3
# =============================================================================
shortLongStates = (min(avgLenBridges, key=avgLenBridges.get), \
                   max(avgLenBridges, key=avgLenBridges.get))

# =============================================================================
# Question 1.4
# =============================================================================
L4 = list(filter(test3.q4_condition,L1))
diff = []
for i in range (len(L4)):
    diff.append(L4[i][3] - L4[i][2])
avgRebuilt = stats.mean(diff)

# =============================================================================
# Question 1.5
# =============================================================================
#clean the format of the array of lists for 00 and 10 year
for i in range(len(list_10)):
    list_10[i] = [test3.myfloat(list_10[i][3:18]), \
                  test3.myfloat(list_10[i][0:3]), \
                  test3.myfloat(list_10[i][156:160]),\
                  test3.myfloat(list_10[i][361:365]), \
                  test3.myfloat(list_10[i][222:228]),\
                  test3.myfloat(list_10[i][164:170])]
for i in range(len(list_00)):
    list_00[i] = [test3.myfloat(list_00[i][3:18]),\
                  test3.myfloat(list_00[i][0:3]), \
                  test3.myfloat(list_00[i][156:160]), \
                  test3.myfloat(list_00[i][361:365]), \
                  test3.myfloat(list_00[i][222:228]), \
                  test3.myfloat(list_00[i][164:170])]
#filter according to the condition fucntion
L_10 = list(filter(test3.q1_condition,list_10))
L_00 = list(filter(test3.q1_condition,list_00))

for i in range(len(L_00)):
    L_00[i] = [str(L_00[i][0:3]), L_00[i][-1]]
for i in range(len(L_10)):
    L_10[i] = [str(L_10[i][0:3]), L_10[i][-1]]
    
temp_dict = dict
com_x = temp_dict(L_00)
com_y = temp_dict(L_10)
out = [[temp_dict, com_x[temp_dict], \
        com_y[temp_dict]] for temp_dict in com_x if temp_dict in com_y]    
new_out = list(filter(test3.filt_nan, out))
count_inc = 0
for elements in new_out:
    if elements[1] < elements[2]:
        count_inc += 1
propIncTraffic = count_inc/len(new_out)


# =============================================================================
# Question 1.6
# =============================================================================
#empty list for storing average
avg = []
for elements in new_out:
    try: 
        per = abs((elements[2]-elements[1]))/elements[1]
        avg.append(per)
    except ZeroDivisionError :
        pass
avgPercentChange = stats.mean(avg)



#delete the unessary variables for the ease of grading
del L1, L4, L_temp, avg, com_x, com_y, count_inc, diff, dir_list, elem, \
elements, file_list, file_name, i, j, key, l00, l05, l10, list_00, \
list_05, list_10, new_out, out, path, per, state

#remove all the unzipped files //cleaning 
os.system("rm -rf ./*10.txt")
os.system("rm -rf ./*00.txt")
os.system("rm -rf ./*05.txt")











