# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 05:34:18 2017

@author: Administrator
"""

# Import useful libraries
import gdeltxp
import gdeltviz
import operator
import scipy as sp
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from math import isnan
from collections import Counter
from collections import OrderedDict 
plt.style.use('seaborn-whitegrid')

# Declare global variables
all_events = pd.read_csv('C:/Users/Administrator/Dropbox/GDELT/all_events.csv').sort_values('SQLDATE', ascending=1)
goldstein_codes = pd.read_csv('C:/Users/Administrator/Dropbox/GDELT/goldstein_codes.csv')
event_codes = pd.read_csv('C:/Users/Administrator/Dropbox/GDELT/event_codes.csv')
events, goldstein = {}, {}

# Populate event names dictionary
for index, row in event_codes.iterrows():
    events[row.CAMEOEVENTCODE] = row.EVENTDESCRIPTION
events[106] = 'unknown'

# Populate goldstein scale dictionary
for index, row in goldstein_codes.iterrows():
    goldstein[int(row.CAMEOEVENTCODE)] = row.GOLDSTEINSCALE
goldstein[106] = 0

#print(all_events.columns)
#print(goldstein_codes.columns)
#print(event_codes.columns)

# Event Summary
gdeltxp.eventsSummary(all_events)

# Actor Type Codes Counts
ActorType1Codes = gdeltxp.actorType1Codes(all_events)
print(ActorType1Codes)

# Actor Type Code Pie Chart
gdeltviz.pieChart(list(ActorType1Codes.keys()), list(ActorType1Codes.values()))

# Prominent Actors
ActorNames = gdeltxp.actorNames(all_events)
print(ActorNames)

# Prominent Actors Visualization
gdeltviz.pieChart(list(ActorNames.keys()), list(ActorNames.values()))

dates = sorted([key for key in Counter(all_events['SQLDATE']).keys()])
farc1 = [all_events.loc[all_events['SQLDATE'] == date].loc[all_events['Actor1Name'] == 'FARC', 'GoldsteinScale'].sum() for date in dates] # / (len(all_events.loc[all_events['SQLDATE'] == date].loc[all_events['Actor1Name'] == 'FARC', 'GoldsteinScale'])+1)
farc2 = [all_events.loc[all_events['SQLDATE'] == date].loc[all_events['Actor2Name'] == 'FARC', 'GoldsteinScale'].sum() for date in dates] # / (len(all_events.loc[all_events['SQLDATE'] == date].loc[all_events['Actor2Name'] == 'FARC', 'GoldsteinScale'])+1)
window = 1
farc = gdeltxp.movingAverage([farc1[i] + farc2[i] for i in range(len(farc1))], window)
print(farc[:10])