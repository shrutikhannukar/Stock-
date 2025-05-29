import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from datetime import timedelta

def predict_prices(historical_data, forecast_days=5):
    """
    Predict future stock prices based on historical data.

    Parameters:
        historical_data (pd.DataFrame): DataFrame containing 'date' and 'price' columns.
        forecast_days (int): Number of days to forecast.

    Returns:
        dict: Dictionary containing predicted prices for the next `forecast_days`.
    """
    # Convert 'date' to a numeric value for modeling
    historical_data['date_numeric'] = (pd.to_datetime(historical_data['date']) - pd.Timestamp("1970-01-01")).dt.days

    # Features (X) and Target (y)
    X = historical_data[['date_numeric']]
    y = historical_data['price']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Test the model (Optional: Evaluate)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model Mean Squared Error: {mse}")

    # Forecast future prices
    last_date = historical_data['date'].max()
    future_dates = [(last_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1, forecast_days + 1)]
    future_date_numeric = [(pd.to_datetime(date) - pd.Timestamp("1970-01-01")).days for date in future_dates]

    future_prices = model.predict(np.array(future_date_numeric).reshape(-1, 1))
    return dict(zip(future_dates, future_prices))

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from django.utils.timezone import now, timedelta
from .models import StockData, StockPrediction
import random
from datetime import datetime, timedelta

def predict_prices_for_ticker(ticker):
    """
    Generate mock predictions for the next 7 days for the given stock ticker.
    """
    try:
        # Get the current date
        current_date = datetime.now().date()

        # Mock logic for price prediction
        last_price = StockData.objects.filter(ticker=ticker).order_by('-timestamp').first().close_price
        predictions = []

        for day in range(1, 8):  # Predict for the next 7 days
            prediction_date = current_date + timedelta(days=int(day))  # Convert day to Python int
            predicted_price = last_price * (1 + (random.uniform(-0.02, 0.02)))  # +/- 2% variation
            predictions.append({'date': prediction_date, 'price': round(predicted_price, 2)})

            # Save prediction in the database
            StockPrediction.objects.create(
                ticker=ticker,
                prediction_date=prediction_date,
                predicted_price=round(predicted_price, 2)
            )
        return predictions
    except Exception as e:
        raise ValueError(f"Error generating predictions for {ticker}: {e}")
