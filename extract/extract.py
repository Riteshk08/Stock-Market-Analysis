from .utils import *
# from utils import check_database, check_folder, fetch_stock_from_yahoo, get_connection_string

def get_stock_data(ticker, start_dt, end_dt, interval):
    '''
    Aim of this function to check if the stock data is available in the database or data folder.
    If the stock data is not available it will fetch the stock data from yfinance.
    This function can be extended to AWS/GCP or any other cloud provider. 
    '''

    #data, isPresent = check_database(ticker_name=ticker)
    isPresent = False
    # Check if the data is already in the database 
    if isPresent:
        return data
    elif not isPresent:
        result = check_folder(ticker_name=ticker, folder_name="data\\processed\\")
        if result is not None:
            return result
        else:
            return fetch_stock_from_yahoo(ticker, start_dt, end_dt, interval)
        
