import yfinance as yf
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
from sklearn.preprocessing import StandardScaler
from datetime import datetime, timedelta
import pandas as pd

def get_data(ticker):
    stock_data = yf.download(ticker, start='2024-01-01')
    return stock_data['Close']

def stationary_check(close_price):
    adf_test = adfuller(close_price)
    p_value = round(adf_test[1], 3)
    return p_value

def get_rolling_mean(close_price):
    rolling_price = close_price.rolling(window=7).mean().dropna()
    return rolling_price

def get_differencing_order(close_price):
    p_value = stationary_check(close_price)
    d = 0
    while True:
        if p_value > 0.05:
            d += 1
            close_price = close_price.diff().dropna()
            p_value = stationary_check(close_price)
        else:
            break
    return d
def fit_model(data, differencing_order):
    model = ARIMA(data, order=(30, differencing_order, 30))
    model_fit = model.fit()
    
    forecast_steps = 30
    forecast = model_fit.get_forecast(steps=forecast_steps)
    
    predictions = forecast.predicted_mean
    return predictions

def evaluate_model(original_price, differencing_order):
    train_data, test_data = original_price[:-30], original_price[-30:]
    predictions = fit_model(train_data, differencing_order)
    rmse = np.sqrt(mean_squared_error(test_data, predictions))
    return round(rmse, 2)

def scaling(close_price):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(np.array(close_price).reshape(-1, 1))
    return scaled_data, scaler

def get_forecast(original_price, differencing_order):
    predictions = fit_model(original_price, differencing_order)
    start_date = datetime.now().strftime('%Y-%m-%d')
    end_date = (datetime.now() + timedelta(days=29)).strftime('%Y-%m-%d')
    forecast_index = pd.date_range(start=start_date, end=end_date, freq='D')
    forecast_df = pd.DataFrame(predictions, index=forecast_index, columns=['Close'])
    return forecast_df

def inverse_scaling(scaler, scaled_data):
    close_price = scaler.inverse_transform(np.array(scaled_data).reshape(-1, 1))
    return close_price
