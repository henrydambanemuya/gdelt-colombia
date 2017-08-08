# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 20:25:44 2017

@author: Administrator
"""
import numpy as np
import seaborn as sns
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from collections import Counter

def heatmap(dataframe):
    corr = dataframe.corr(method='pearson')    
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    #print(corr)
    return sns.heatmap(corr, mask=mask, cmap=sns.diverging_palette(10, 240, as_cmap=True), vmax=1, vmin=-1, square=True, linewidths=.5, cbar_kws={"shrink": .5})


def pieChart(labels, sizes):
    fig, ax = plt.subplots(figsize=(8, 8))
    patches, texts = plt.pie(sizes, colors=cm.Set3(np.linspace(0, 1, len(sizes))), startangle=90)
    plt.legend(patches, labels, loc="right", fontsize=15)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    
def goldsteinScatter(dataframe, events, goldstein):
    event_code_frequency = Counter(dataframe.EventRootCode)

    event_names = [events[key] for key in Counter(dataframe.EventRootCode).keys()]
    event_frequency = [event_code_frequency[key] for key in Counter(dataframe.EventRootCode).keys()]
    event_goldstein = [goldstein[key]for key in Counter(dataframe.EventRootCode).keys()]
    colors = []
    
    print('EVENT ROOT CODE: Goldstein, Frequency')
    for i in range(len(event_names)):
        print('{}: {}, {}'.format(event_names[i], event_goldstein[i], event_frequency[i]))
    
    for value in event_goldstein:
        if value < 0:
            colors.append('r')
        elif value > 0:
            colors.append('g')
        else:
            colors.append('b')
            
    ind = np.arange(-10, 11, 1)
           
    fig, ax = plt.subplots(figsize= (18, 8))
    ax.set_title('', fontsize=15, fontweight='bold')
    plt.scatter(event_goldstein,event_frequency, c=colors, s=120)
    plt.axhline(y=1000, color='k', linestyle='--')
    plt.axvline(x=0, color='k', linestyle='--')
    ax.set_xticks(ind)
    ax.set_yscale('log')
    ax.set_xlabel('Goldstein Scale', fontsize=18)
    ax.set_ylabel('Frequency' , fontsize=18)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    plt.tight_layout()
    plt.xlim([-11,11])
    plt.ylim([0,100000])
    plt.show()