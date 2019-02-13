#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 23:11:15 2018

@author: zizhaozhang
@UMID: 35009521
"""
# =============================================================================
# relevant packages and module
# =============================================================================
import pandas as pd
# =============================================================================
# Question 3.1
# =============================================================================
df_trips = pd.read_csv("./trips.csv")
trips1 = df_trips[(df_trips['pickup_latitude'] < 41.5) &
         (df_trips['pickup_latitude'] > 40) &
         (df_trips['pickup_longitude'] > -75) &
         (df_trips['pickup_longitude'] < -72) &
         (df_trips['passenger_count'] > 0) &
         (df_trips['passenger_count'] < 5) &
         (df_trips['trip_time_in_secs'] > 1800)] 
# =============================================================================
# Question 3.2
# =============================================================================
tripStats = (len(trips1), trips1["passenger_count"].mean(), \
                  trips1["trip_time_in_secs"].mean(), \
                  trips1["trip_time_in_secs"].std())
# =============================================================================
# Question 3.3
# =============================================================================
#reads in the zip codes and seperate the coords
zip_raw = pd.read_csv("./zipcodes.csv")
zip_raw["pickup_latitude"], \
 zip_raw["pickup_longitude"] = zip_raw["Coords"].str.split(',',1).str
zip_raw["pickup_longitude"] = zip_raw["pickup_longitude"].apply(float)
zip_raw["pickup_latitude"] = zip_raw["pickup_latitude"].apply(float)
#remove index unwanted
zip_raw = zip_raw.drop(["Unnamed: 0"],axis =1)
#rounds up the digits to 2
trips1 = trips1.round({"pickup_longitude": 2,"pickup_latitude": 2 })
trips1 = trips1.drop(["Unnamed: 0"],axis =1)
#merge the two data frames
trips2 = pd.merge( trips1 , zip_raw, \
                       on = ["pickup_longitude", "pickup_latitude"])
trips2 = trips2.drop(["Coords"],axis=1)
#remove nas
trips2 = trips2.dropna()

# =============================================================================
# Question 3.4
# =============================================================================
trips2_cp =  trips2.copy()
trips2_cp["Day"], \
trips2_cp["Hour"] = trips2_cp["pickup_datetime"].str.split(' ',1).str
trips2_cp["Hour"] = trips2_cp["Hour"].map(lambda x: str(x)[:-6])
trips2_cp["Day"] = trips2_cp["Day"].map(lambda x: str(x)[-2:])
trips2_cp["Hour"] = trips2_cp["Hour"].apply(int)
trips2_cp["Day"] = trips2_cp["Day"].apply(int)
trips3 = trips2_cp.groupby(["Zipcode","Day","Hour"])["trip_time_in_secs"]. \
    count().reset_index(name="Count")
# =============================================================================
# Question 3.5
# =============================================================================
df_weather = pd.read_csv('./weather.csv')
trips3_cp = trips3.copy()
trips4 = pd.merge(trips3,df_weather,on = ["Day","Hour"])
# =============================================================================
# Question 3.6
# =============================================================================
import datetime
trips5 = trips4.copy()
trips5["Weekday"] = [datetime.date(2013,1,trips5.Day[i]).weekday() for i \
      in range(0, len(trips5))]
trips5_col = trips5.columns.tolist()
trips5_col = ['Zipcode', 'Count','Day', 'Hour', 'Weekday', \
              'Temp', 'Icon', 'Rain', 'Snow']
trips5 = trips5[trips5_col] 
# =============================================================================
# Question 3.7
# =============================================================================
trips6 = trips5.loc[trips5.Count>1,:]
# =============================================================================
# Question 3.8
# =============================================================================
import matplotlib.pyplot as plt
fig, axis1 = plt.subplots(figsize=(10,5))
axis2 = axis1.twinx()
trips5.groupby(['Hour']).sum()['Count'].plot(ax = axis1,color = 'g')
axis1.set_ylabel('Total Number of taxi trips', color='g')
trips5.groupby(['Hour']).mean()['Temp'].plot(ax = axis2,color = 'r')
axis2.set_ylabel('average temperature', color='r')
# =============================================================================
# explanation of the trends:
# =============================================================================

'''
As the plot shown in the right panel, which the green trend line stands for the
Total Number of taxi trips, while the red trend line stands for the 
average temprature. The trends tells me that both the trend of temperature 
and trips reaches aournd 3pm in the afternoon. However, before 3pm. 
for each steep drop of the temperature follows by a steep increasing trend 
in the trips by taxi. Indicating the quicker the temperatue drops, 
the increase of the amount of customers ride taxis expedites.

'''

# =============================================================================
# Question 3.9
#reference: lecture 11-607
#url as below
#https://github.com/marcio-mourao/Stats607-Fall2018/blob/master/Lecture11.ipynb
# =============================================================================
#3.9
import numpy as np
#from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import statsmodels.formula.api as smf 
import statsmodels.api as sm
#==============================================================================
#make a copy and factorize all the categoricals
#check types in dataframe
#trips6.dtypes
trips6_cp = trips6.copy()
trips6_cp["Icon"] = pd.factorize(trips6_cp["Icon"])[0]
#set up X and y
X = trips6_cp.loc[:,["Zipcode","Weekday","Hour","Temp","Icon"]]
y = trips6_cp["Count"].values
X_train, X_test, y_train, y_test = train_test_split(X, y, \
    random_state=  1234, test_size = 0.2)
random_forest = RandomForestRegressor(criterion='mse')
#set the parameter grid:
RFOpts = {'max_features': np.arange(4,5), 'n_estimators': np.arange(40,250,10)}
gridCV = GridSearchCV(random_forest, cv = 2, param_grid = RFOpts, \
    return_train_score=True)
modelGrid = gridCV.fit(X_train, y_train)
#print(modelGrid.best_params_)
#print(np.round(modelGrid.best_score_,2))
y_pred_class = modelGrid.predict(X_test)
rmseResults_RF = mean_squared_error(y_test,y_pred_class)
model_nbi = smf.GLM(y_train, X_train, \
                family = sm.families.NegativeBinomial()).fit().predict(X_test)
#assign the rmsResults
mse_Bi = mean_squared_error(y_test, model_nbi)
rmseResults = (mse_Bi,rmseResults_RF)


#clear unessary output at the end, easier for the grading

del RFOpts, X, X_test, X_train, df_trips, df_weather, model_nbi, \
    mse_Bi, rmseResults_RF, trips2_cp, trips3_cp, trips5_col, \
    trips6_cp, y, y_pred_class, y_train, y_test, zip_raw





























