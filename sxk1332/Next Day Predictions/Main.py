import os
from datetime import date
import pandas as pd
import yfinance as yf

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import warnings
import papermill as pm
import sys
warnings.filterwarnings("ignore")
sys.path.append("C:\\FYP\\sxk1332\\Next Day Predictions")
import Common_Functions


#First run the sentiment analysis notebook to get the most recent news articles 

print("Updating Sentiment Analysis Scores...")
pm.execute_notebook(
    'C:\\FYP\\sxk1332\\Next Day Predictions\\SentimentAnalysis.ipynb',
    'C:\\FYP\\sxk1332\\Next Day Predictions\\Output Notebooks\\SentimentAnalysis_Output.ipynb',
    log_output=False
)
print("Sentiment Scores Successfully Updated")


#Then run all the notebooks for next day predictions, and save ouputs to SQL

print("Running LSTM Close Model...")
pm.execute_notebook(
    'C:\\FYP\\sxk1332\\Next Day Predictions\\LSTM_Close.ipynb',
    'C:\\FYP\\sxk1332\\Next Day Predictions\\Output Notebooks\\LSTM_Close_Output.ipynb',
    log_output=False
)
print("Next Day Close price saved to SQL")

print("Running LSTM Directions Model...")
pm.execute_notebook(
    'C:\\FYP\\sxk1332\\Next Day Predictions\\LSTM_Direction.ipynb',
    'C:\\FYP\\sxk1332\\Next Day Predictions\\Output Notebooks\\LSTM_Direction_Ouput.ipynb',
    log_output=False
)
print("Next Day Direction saved to SQL")

print("Running LSTM Returns Directions Model...")
pm.execute_notebook(
    'C:\\FYP\\sxk1332\\Next Day Predictions\\LSTM_Returns_Direction.ipynb',
    'C:\\FYP\\sxk1332\\Next Day Predictions\\Output Notebooks\\LSTM_Returns_Direction_Output.ipynb',
    log_output=False
)
print("Next Day Returns Direction saved to SQL")


#Get the model update Actual Close price within SQL

#First downloads 2 days rather than 1 to act as a safety net in case code is run on Sunday but last actual price was Friday
ticker = 'AAPL'  
data = yf.download(ticker, period="2d")

data.reset_index(inplace=True)

if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

latest_row = data.iloc[-1]

date_value = latest_row["Date"].strftime("%Y-%m-%d")
close_price = round(latest_row["Close"], 2)

#Call the column fuction and update the 'ActualPrice' as the last step
Common_Functions.WriteToDatabase("Update",date_value,"ActualPrice",close_price)

print("All model predictions updated successfully.") 

