import pandas as pd
class DataHandler:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

    def stream_data(self):
        for i in range(len(self.data)):
            yield self.data.index[i], self.data.iloc[i]
    