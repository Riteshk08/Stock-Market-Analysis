import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
from .config import Config
import os
import yfinance as yf


def get_connection_string():
    '''
    this function returns the connection string
    '''
    c = Config()
    connection_string = f'mysql+mysqlconnector://{c.username}:{c.password}@{c.host}:{c.port}/{c.database}'
    return connection_string

def check_database(ticker_name):
    '''
    this method checks if the data already exists in the database or not
    '''
    connection_string = get_connection_string()
    # Create a SQLAlchemy engine
    engine = create_engine(connection_string)
    meta = MetaData()
    # Connect to MySQL database
    table_name = ticker_name

    # Reflect the table structure from the database
    table = Table(table_name, meta, autoload=True, autoload_with=engine)

    # Connect to the database
    with engine.connect() as connection:
        # Build a select statement to count rows in the table
        select_stmt = table.select().count()

        # Execute the select statement
        result = connection.execute(select_stmt)

        # Fetch the count of rows
        row_count = result.scalar()

        # Check if data exists
        if row_count > 0:
            print("Data exists in the table.")
            return result, True
        else:
            print("No data found in the table.")
            return None, False

def check_folder(ticker_name, folder_name=None):
    '''
    this method checks if the data already exists in the folder or not
    '''
    
    filename = os.path.join(folder_name,ticker_name)
    try:
        data = pd.read_csv(filename+".csv")
    except FileNotFoundError as exception:
        print("Could not find file %s" % filename, exception)
        data = None
    if data is None:
        return None
    else:
        return data

def fetch_stock_from_yahoo(tickers, start_dt, end_dt, interval='1d'):
    '''
    fetch stock data from yahoo based on start_dt and end_dt and given interval
    '''
    start_date = pd.to_datetime(start_dt)
    end_date = pd.to_datetime(end_dt)
    
    period_limit = pd.DateOffset(months=1)
    stock_data = pd.DataFrame()
    
    while start_date <= end_date:
        # Calculate the end date for this period
        period_end = min(start_date + period_limit, end_date)

        # Download stock data for this period
        print(tickers)
        data = yf.download(tickers.strip(), start=start_date, end=period_end, interval=interval)

        # Concatenate the data with the existing DataFrame
        stock_data = pd.concat([stock_data, data])

        # Move to the next period
        start_date = period_end + pd.Timedelta(days=1)
    
    stock_data.to_csv("data\\raw\\" + tickers+".csv",index = True)
    return stock_data


