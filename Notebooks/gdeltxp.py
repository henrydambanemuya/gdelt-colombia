# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 20:35:36 2017

@author: Administrator
"""
import numpy as np
from math import isnan
from collections import Counter, OrderedDict

def eventsSummary(dataframe):
    print('Total Events: %s'  %len(dataframe))
    print('Total Sources: %s'  %sum(dataframe.NumSources))
    print('Total Articles: %s'  %sum(dataframe.NumArticles))
    print('Total Mentions: %s'  %sum(dataframe.NumMentions))
    #print('Global Tone: ', dataframe.AvgTone.describe())
    #print('Global Tone: ', dataframe.GoldsteinScale.describe())
    
def actorNames(dataframe):
    # Preprocessing: Prominent Actors
    ActorNames = Counter(dataframe.Actor1Name) + Counter(dataframe.Actor2Name)
    StopNames = ['COLOMBIA', 'COLOMBIAN', 'BOGOTA', 'BARRANQUILLA', 'MEDELLIN', 'BANCOLOMBIA', 'BUCARAMANGA']
    
    for value in ActorNames.keys():
        try:
            if isnan(value):
                del ActorNames[value]
                break
        except:
            continue
    
    for name in StopNames:
        del ActorNames[name]
    
    return OrderedDict(sorted(ActorNames.items(), key=lambda x: x[1], reverse=True))

def actorType1Codes(dataframe):
    ActorType1Codes = Counter(dataframe.Actor1Type1Code) + Counter(dataframe.Actor2Type1Code)
    
    for value in ActorType1Codes.keys():
        try:
            if isnan(value):
                del ActorType1Codes[value]
                break
        except:
            continue
    
    return OrderedDict(sorted(ActorType1Codes.items(), key=lambda x: x[1], reverse=True))

def movingAverage(values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma 