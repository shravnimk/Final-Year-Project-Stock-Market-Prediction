Project Description: 
In the final year of my BSc Artificial Intelligence / Computer Science degree, I completed a research project in Python, evaluating whether different deep learning architectures could generate useful stock predictions.
In this project, I compared an LSTM, CNN, CNN-LSTM, and a Transformer model for next-day Apple stock price prediction. Each model is trained on 10 years of historical OHLCV data, with experiments performed to assess whether incorporating technical indicators and financial news sentiment features improve predictive performance. Models are evaluated using statistical error metrics, directional accuracy and a backtesting framework was designed to assess whether model predictions can be translated into a profitable trading strategy. The best performing model (LSTM) was also extended to forecast directional movements and returns, testing its suitability for generating predictions on live market data. The generated predictions were then saved into SQL and used to generate reports in Excel.  

Project Navigation:
Baseline Models: Contains all deep learning models (LSTM, CNN, CNN-LSTM, Transformer) only trained on OHLCV (Open, High, Low, Close & Volume) data to establish a baseline for evaluating whether incorporating technical indicators and sentiment features would improve predictive performance.

Correlation Matrix: Shows the code I used to to select the most relevant features to feed my models using a feature selection method (Spearman correlation and Mutual Information)

Comparing Models: Contains all deep learning models trained on OHLCV data and additional features and such as average daily sentiment scores, and technical indicators chosen through the feature selection method.

Backtesting: Shows the results and backtesting strategy I implemented - incorporating predicted returns, sentiment-based trading signals, volatility-adjusted position sizing and transaction costs to simulate trading under realistic market conditions

Next day predictions: Shows the code for generating directional movement predictions on live market data and saving the results into SQL. To automate the process, a main script using Papermill was used to first retrieve the latest news articles and converted them into sentiment scores and a common ‘WriteToDatabase’ function was implemented to manage all database writes. 

15-Minute Models: Shows results of all deep learning models trained on 15-minute interval data instead of daily data in an attempt to increase the size of the training dataset. 

Failed Experiments: Tree-based ensemble methods, specifically Random Forest and XGBoost were implemented as benchmark models for predicting next day closing price, to compare their performance against more complex deep learning architectures.

Documentation: Contains my final year report, an excel report of my generated directional movement predictions from the LSTM, and a dairy I kept to track the process across my entire project. 
