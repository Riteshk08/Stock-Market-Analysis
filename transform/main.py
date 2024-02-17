import pandas as pd

def remove_outliers_3sigma(df, column):
    '''Calculate mean and standard deviation to find outliers using 3 sigma rules'''
    mean = df[column].mean()
    std_dev = df[column].std()
    
    # Define the upper and lower bounds
    lower_bound = mean - 3 * std_dev
    upper_bound = mean + 3 * std_dev
    
    # Identify outliers
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    
    return outliers, lower_bound, upper_bound

def impute_outliers_mean(df, column, lower_bound, upper_bound):
    '''Calculate mean to impute outliers, similarly we can use median, near back or near front to fill outliers'''
    mean = df[column].mean()
    
    # Replace outliers with mean
    df.loc[(df[column] < lower_bound) | (df[column] > upper_bound), column] = mean
    
    return df

def remove_outlier(data):
    ''' this removes outliers'''

    cols = ['Open', 'Close', 'High', 'Low']
    for col in cols:
        outliers, lb, ub =  remove_outliers_3sigma(data, col)
        print('Outlier found in column ' + str(col), len(outliers))
        data = impute_outliers_mean(data, col, lb, ub)

    

def transform_data(data):
    ''' transform data into proper format and return processed data'''
    data['date'] = pd.to_datetime(data.index, errors='coerce')
    data['Open'] = data['Open'].fillna(method='ffill')
    data['Close'] = data['Close'].fillna(method='ffill')
    data['High'] = data['High'].fillna(method='ffill')
    data['Low'] = data['Low'].fillna(method='ffill')
    
    remove_outlier(data)
    return data

