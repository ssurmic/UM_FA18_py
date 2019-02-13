# -*- coding: utf-8 -*-
"""
@author: Zizhao Zhang
@UMID:   35009521

"""
# =============================================================================
# set up global scope for below functions' usages
# =============================================================================
# CAPs
MURDER_INDEX = 3
ASSULT_INDEX = 6
VIOLENT_CRIME_TOTAL_INDEX = 2
PROPERTY_CRIME_TOTAL_INDEX = 7
BURGLARY_INDEX = 8
VEHICLE_THEFT_INDEX = 10
LAST_COLUMN_INDEX = 10
POPULATION_SAMPLE = 100000
VIOLENT_CRIME_INDEX = 2


# =============================================================================
# question: 1.1
# =============================================================================

import assignment1_Data as a1Data

crime = a1Data.get_US_crime()
crime_rates = a1Data.get_US_crime_rates()

# =============================================================================
# question: 1.2
# =============================================================================

def equal_length(nested_list):
    #check if all lists' length are the same for nested list
    return all(len(i) == len(nested_list[0]) for i in nested_list) 

# =============================================================================
# question: 1.3
# =============================================================================
    
def get_states(crime_list):
    #return a list of every first element within the sublists of nested list
    state_list = list([sub_list[0] for sub_list in crime_list])
    #pop total
    state_list.pop()
    return state_list
    
# =============================================================================
# question 1.4
# =============================================================================
    
def equal_vc(crime_list):
    #transpose the matrix to put the total in a single list
    v_crime_total = list(map(list, zip(*crime_list)))[VIOLENT_CRIME_TOTAL_INDEX]
    #initiate a list to calculate sums
    sum_list = []
    for items in crime_list:
        sum_list.append(sum(items[MURDER_INDEX: ASSULT_INDEX + 1]))
    return(sum_list == v_crime_total)
    
    
def equal_pc(crime_list):
    #transpose the matrix to put the total in a single list
    p_crime_total = list(map(list, zip(*crime_list)))[PROPERTY_CRIME_TOTAL_INDEX]
    #initiate a list to calculate sums
    sum_list = []
    for items in crime_list:
        sum_list.append(sum(items[BURGLARY_INDEX:VEHICLE_THEFT_INDEX + 1]))
    return(sum_list == p_crime_total)
    
# =============================================================================
# question 1.5
# =============================================================================
    
def skip_last_row(crime_list):
    # return a new list without the last row of the original list
    return list(crime_list[i] for i in range(len(crime_list)-1))
#initiate a list of components for comparison
components = []
def equal_total(crime_list):
    #initiate a newlist without the last row of total sum of data
    new_list = skip_last_row(crime_list)
    #traverse through all the column of new list, 
    # and compare the sums with original sum
    for i in range(1,LAST_COLUMN_INDEX + 1):
        components.append (sum([item[i] for item in new_list ]))
    return (components == crime_list[len(crime_list)-1][1:LAST_COLUMN_INDEX + 1])

# =============================================================================
# question 1.6
# =============================================================================
    
#import copy for deepcopy usage
import copy as cp
def get_crime_rate(crime_list):
    crimeRatesCopy = cp.deepcopy(crime_list)
    #initiate a list for result storeage
    new_rate_list = []
    #recalculate the rate
    for i in range (2,LAST_COLUMN_INDEX + 1):
        new_rate_list.append(([round((item[i]/item[1]*POPULATION_SAMPLE),1) 
        for item in crimeRatesCopy ]))
    #transpose the list of lists
    new_rate_list = list(map(list, zip(*new_rate_list)))
    for row in crimeRatesCopy:
        del row[2:len(crimeRatesCopy)]
    #merge list of lists and return crimeRates

    crimeRates = [a  + b for a, b in zip(crimeRatesCopy,new_rate_list)]   
    return crimeRates

# =============================================================================
# question 1.7
# =============================================================================
    
#import random
import random as rand
#input n is the number of comparisons
def equal_rates(crime_rates,n):
    if n >= 1 :
        #assign crimeRatesOriginal
        crimeRatesOriginal = a1Data.get_US_crime_rates()
        #assign my crimeRates
        crimeRates = get_crime_rate(crime)
        #initiate lists for storage
        list1 = []
        list2 = []
        for i in range(1, n+1):
            #assign row numbers
            index = rand.randint(0, len(crime_rates)-1)
            list1.append(crimeRatesOriginal[index])
            list2.append(crimeRates[index])          
        return list1, list2, list1 == list2
    else:
        return "please enter an integer n at least 1"
    
# =============================================================================
# question 1.8
# =============================================================================
        
def top5_violent_states(crime_rates):
    #crime_rates_copy
    crime_rates_new = cp.deepcopy(crime_rates)
    #pop total
    crime_rates_new = skip_last_row(crime_rates_new)
    #sort reversely
    crime_rates_new.sort(key=lambda x: x[VIOLENT_CRIME_INDEX ], reverse = True)
    top_crime_dic = {item[0]: item[VIOLENT_CRIME_INDEX ] for item in 
                     crime_rates_new}
    top_5_crime_dic = {i: top_crime_dic[i] for i in list(top_crime_dic)[:5]}
    return(top_5_crime_dic)
    
# =============================================================================
# question 1.9
# =============================================================================
#define a indexCrime dictionary as global var
#please enter the indexCrime parameter as the value in the dictionary
crime_dictionary = {'Violent Crime rate':2, 
              'Murder and nonnegligent manslaughter rate': 3,
              'Rape':4,
              'Robbery rate':5,
              'Aggravated assault rate':6,
              'Property crime rate':7,
              'Burglary rate':8,
              'Larceny-theft rate':9,
              'Motor vehicle theft rate':10}

def top_crime_states(crime_rates, n, indexCrime):
    crime_rates_new = cp.deepcopy(crime_rates)
    #pop total
    crime_rates_new = skip_last_row(crime_rates_new)
    #make sure that n is proper
    if n > 52:
        return "please enter n less or equal than 52"
    #make sure index is proper
    elif indexCrime in crime_dictionary.values():
        #reverse sort
        crime_rates_new.sort(key=lambda x: x[indexCrime]
        , reverse = True)
        top_crime_dic = {item[0]: item[indexCrime] for item in crime_rates_new}
        top_n_crime_dic = {i: top_crime_dic[i] for i in list(top_crime_dic)[:n]}
        return(top_n_crime_dic)   
    else:
        return "indexCrime is an invalid index"
    
# =============================================================================
# question 1.10
# =============================================================================
        
import statistics as stats
def crimes_stats(crime_rates, indexCrime):
    crime_rates_new = cp.deepcopy(crime_rates)
    #make sure that indexCrime is proper
    if indexCrime in crime_dictionary.values():
        #transpose the list of lists
        transpose_rates = list(map(list, zip(*crime_rates_new)))
        #assign statistics
        mean = stats.mean(transpose_rates[indexCrime])
        standard_deviation = stats.stdev(transpose_rates[indexCrime])
        variance = stats.variance(transpose_rates[indexCrime])
        return mean, standard_deviation, variance
    else:
        return "indexCrime is an invalid index"
    
# =============================================================================
# end
# =============================================================================




