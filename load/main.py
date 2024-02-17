from extract.extract import get_connection_string, create_engine

def store_data(data, ticker, to_database = False):
    # Create a SQLAlchemy engine
    if to_database:
        connection_string = get_connection_string(ticker)

        engine = create_engine(connection_string)

        # Export DataFrame to MySQL
        data.to_sql('Stock_table', engine, index=False, if_exists='replace')

        print("DataFrame exported to MySQL successfully.")

    else:
        data.to_csv("data\\processed\\"+ticker+".csv", index=False)