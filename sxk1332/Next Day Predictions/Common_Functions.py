from datetime import date,datetime, timedelta
import pyodbc 
from sqlalchemy import create_engine

#Financial data
import yfinance as yf


#Data manipulation and numerical computing
import numpy as np
import pandas as pd

#Technical Indicators 
import ta
from ta.trend import SMAIndicator
from ta.momentum import RSIIndicator
from ta.volatility import AverageTrueRange
from ta.volume import OnBalanceVolumeIndicator 


def WriteToDatabase(Mode,PrectionDate,ColumnName=None,Prediction=None):
    server = 'SHRAVNI'
    database = 'StockPrediction'
    username = 'Stock'
    password = 'Stock'
    
    conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password}'
        )

    cursor = conn.cursor()
    
    #First check if a record already exists for that date, to avoid duplicate rows of data
    if Mode == 'Insert':
        SQLString = "Select 1 from NextdayPrediction Where CurrentDate = ?"
        cursor.execute(SQLString, str(PrectionDate))
        RetVal = cursor.fetchone()
        #If the record already exists, do nothing
        if RetVal: 
            print("A record already exists, so don't save another entry")

        #First inset a new row to save the LSTM prediction for its corresponding date
        else:
            SQLString = f"INSERT INTO NextdayPrediction (CurrentDate,LSTM_Close_Price) VALUES (?,?)"
            cursor.execute(SQLString, PrectionDate,Prediction)
            
    #For every other call to the common function, update the row instead
    else:
        SQLString = f"Update NextdayPrediction SET {ColumnName} = ? Where   CurrentDate = ? "
        cursor.execute(SQLString, str(Prediction), PrectionDate)

    conn.commit()
    cursor.close()
    conn.close()
