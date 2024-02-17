import matplotlib.pyplot as plt


def calculate_bollinger_bands(data, window_size, num_std):
    '''Calculate rolling mean and standard deviation which helps to calculate Bollinger plotting'''
    rolling_mean = data.rolling(window=window_size).mean()
    rolling_std = data.rolling(window=window_size).std()
    
    # Calculate upper and lower bands
    upper_band = rolling_mean + (rolling_std * num_std)
    lower_band = rolling_mean - (rolling_std * num_std)
    
    return rolling_mean, upper_band, lower_band

    
def visualize_share(ticker, data, window_size=20, num_std=2):
    '''
    This function visualize the bollinger plot, moving average for Close of the stock.
    Currently, it is hard coded for 'Close' similarly we can do for 'High', 'low' and 'Open'.
    '''

    rolling_mean, upper_band, lower_band = calculate_bollinger_bands(data['Close'], window_size, num_std)
    print(data.columns)
    # Visualize Bollinger Bands and actual data

    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='Actual')
    plt.plot(rolling_mean.index, rolling_mean, label=f'Moving Average ({window_size} days)', color='black')
    plt.plot(upper_band.index, upper_band, label=f'Upper Band ({num_std} std)', color='red', linestyle='--')
    plt.plot(lower_band.index, lower_band, label=f'Lower Band ({num_std} std)', color='green', linestyle='--')
    plt.fill_between(upper_band.index, upper_band, lower_band, color='lightgray', alpha=0.3)
    plt.title('Bollinger Bands of '+str(ticker))
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()