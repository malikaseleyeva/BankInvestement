import requests
import pandas as pd
import spark 
# make a class for API call 

class AlphavantageAPI:
    def __init__(self, stock):
        self.url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey=53HU7S3992V5RPQZ'
        r = requests.get(self.url, verify=False)
        data = r.json()
        data = pd.DataFrame(data['Time Series (Daily)']).T  # Transpose to get dates as rows
        columns = data.columns.tolist()
        print(data, columns)

data = AlphavantageAPI("IBM")