import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb 
import yfinance as yf

sb.set_theme()


DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data(self.symbol, self.start, self.end)


    def get_data(self, symbol, start=None, end=None):
        # Feteches and stores historical stock data in a pandas Dataframe
            if start is None or end is None:
                today = pd.Timestamp.today()
                start = today - pd.DateOffset(years=1)
                end = today

            data = yf.download(symbol, start=start, end=end)
            data.index = pd.to_datetime(data.index)
            self.data = data
            self.calc_returns(data)
            return data

    
    def calc_returns(self, data):
        """method that adds change and return columns to data"""
        data['change'] = data['Close'].diff()

        # Logarithmic return
        data['instant_return'] = np.log(data['Close'].shift(1)).round

    
    def plot_return_dist(self):
        """method that plots instantaneous returns as histogram"""
        sb.set(style='whitegrid')
        plt.figure(figsize=(10,6))
        sb.histplot(self.data['instant_return'].dropna(), bins=50, kde=True, color='blue')


    def plot_performance(self):
        """method that plots stock object performance as percent """
        self.data['percent_change'] = self.data['Close'].pct_change().cumsum() * 100
        
        plt.figure(figsize=(10, 6))
        plt.plot(self.data.index, self.data['percent_change'], label='Percent Change', color='blue')
        plt.title(f'Stock Performance: {self.symbol}')
        plt.xlabel('Date')
        plt.ylabel('Percent Change (%)')
        plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
        plt.legend()
        plt.show()
                  

def main():
    test = Stock(symbol='AAPL') # optionally test custom data range
    print(test.data.head)
    test.plot_performance()
    test.plot_return_dist()
    test.plot_performance()

if __name__ == '__main__':
    main() 