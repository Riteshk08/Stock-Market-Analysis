from extract.extract import get_stock_data
from transform.main import transform_data
from load.main import store_data
from visualization.visulalize import visualize_share


def get_share_data(share, start, end, intervals, store = False):
    '''
    helper function to get share data
    '''
    raw_data = get_stock_data(share, start, end, intervals)
    processed_data = transform_data(raw_data)
    if store:
        store_data(processed_data, share)
    return processed_data

def analyze_data(data, moving_average_day=20, standard_deviation=2):
    '''
    helper function to visualize data
    '''
    visualize_share(share, data, moving_average_day, standard_deviation)
    




if __name__=="__main__":
    '''
    This is main function to start the pipeline for collecting stock data and transforming and visulizing data
    '''
    #Enter share name which you want to analyze
    share = 'TCS.NS'
    start = "01-01-2023"
    end = "15-02-2024"
    interval = "60m"
    data = get_share_data(share = share, start = start, end= end, intervals = interval, store = True)
    moving_average_day = 30
    standard_dev = 3
    analyze_data(data, moving_average_day, standard_dev)