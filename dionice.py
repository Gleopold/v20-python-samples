#First do - source /Users/leopoldgabriel/Documents/GitHub/v20-python-samples/src/env/bin/activate
import subprocess as sp
import sys
import pandas as pd
import csv
import io
from pathlib import Path
#Matplotlib dio
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import numpy as np

home="/Users/leopoldgabriel/Documents/GitHub/v20-python-samples/src/env/bin/"

def api(command_in):#executes command in in current v20 directory using installed aliases
    full_path=home+command_in
    output = sp.getoutput(full_path)#executes command
    output = output.split("\n",2)[2]#splits output to get it in pandas format
    
    df = pd.DataFrame()
    df = pd.read_csv(io.StringIO(output), delim_whitespace=True, index_col=None, skiprows=2, skipinitialspace=True,names=["Date", "Time", "Mid", "Open", "High", "Low", "Close", "Volume" ])#create dataframe from api command output
    print(df)
    return df


def plot(df_ha): #plot candlesticks
    df = df_ha
    fig = go.Figure(data=[go.Candlestick(x=df['Time'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

    fig.show()
    print("Done")

def find_trend(df_trend):
    """Find trend in pandas of stocks"""
    df = df_trend
    df['trend'] = np.where(df['Close'] > df['Open'], 'up', 'down')
    print(df)
    return df


def calculate_20ema(df_ema):
    """Calculate 20 EMA"""
    df = df_ema
    df['ema20'] = df['Close'].ewm(span=20, adjust=False).mean()
    print(df)
    return df

def calculate_200ema(df_ema):
    """Calculate 200 EMA"""
    df = df_ema
    df['ema200'] = df['Close'].ewm(span=200, adjust=False).mean()
    print(df)
    return df

output=api("v20-instrument-candles ETH_USD --count 1000")
find_trend(output)
calculate_20ema(output)
calculate_200ema(output)    

print(output)

