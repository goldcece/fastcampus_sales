import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import random
from datetime import datetime, timedelta
import re

def readfunc(path):
    '''
    read the csv file to dataframe

    parameters:
    path(str) : excel file address to put here


    return:
    df(dataframe) : csv dataframe
    
    '''
    df = pd.read_csv(path)
    return df

def korean_apple():
    '''
    change font to the appleGothic
    '''
    plt.rcParams['font.family'] = 'AppleGothic'
    plt.rcParams['axes.unicode_minus'] = False