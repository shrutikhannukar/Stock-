# # stocks/utils.py
# import random
# from django.utils import timezone
# from .models import StockData

# # Function to generate random stock data and save it to the database
# def generate_random_stock_data(ticker, company_name, num_records=100):
#     """
#     Generates random stock data for a given ticker and company name.
#     Saves the data into the StockData model.

#     :param ticker: Stock ticker symbol (e.g., 'TCS.BO')
#     :param company_name: Full name of the company (e.g., 'Tata Consultancy Services')
#     :param num_records: Number of stock data records to generate
#     """
#     for _ in range(num_records):
#         # Generate random stock prices
#         open_price = round(random.uniform(1000, 5000), 2)  # Opening price between 1000 and 5000
#         close_price = round(random.uniform(1000, 5000), 2)  # Closing price between 1000 and 5000
#         high_price = round(random.uniform(open_price, close_price + 100), 2)  # High price above open and close
#         low_price = round(random.uniform(open_price - 100, close_price), 2)  # Low price below open and close
        
#         # Ensure close price is within the high and low range
#         close_price = max(min(close_price, high_price), low_price)

#         # Save the generated stock data to the database
#         StockData.objects.create(
#             ticker=ticker,
#             company_name=company_name,
#             timestamp=timezone.now(),  # Current timestamp
#             open_price=open_price,
#             high_price=high_price,
#             low_price=low_price,
#             close_price=close_price
#         )
#         print(f"Generated data for {ticker}: Open {open_price}, High {high_price}, Low {low_price}, Close {close_price}")

# generate_random_stock_data('TCS.BO', 'Tata Consultancy Services', num_records=100)
# generate_random_stock_data('RELIANCE.NS', 'Reliance Industries', num_records=100)
# generate_random_stock_data('INFY.NS', 'Infosys', num_records=100)
# generate_random_stock_data('HDFCBANK.NS', 'HDFC Bank', num_records=100)
# generate_random_stock_data('ICICIBANK.NS', 'ICICI Bank', num_records=100)
# generate_random_stock_data('SBIN.NS', 'State Bank of India', num_records=100)
# generate_random_stock_data('BHARTIARTL.NS', 'Bharti Airtel', num_records=100)
# generate_random_stock_data('ADANIENT.NS', 'Adani Enterprises', num_records=100)
# generate_random_stock_data('WIPRO.NS', 'Wipro', num_records=100)
# generate_random_stock_data('TATAMOTORS.NS', 'Tata Motors', num_records=100)