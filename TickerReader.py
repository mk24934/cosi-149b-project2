import pandas as pd
from keras.models import load_model
import numpy as np

class TickerReader(object):
    def __init__(self, filename):
        self.df = pd.read_csv(filename)
        self.df = self.df.drop(columns=['open', 'high', 'low', 'close', 'volume', 'dividend', 'split'])
        self.df = self.df.head(10000).sort_values(by=['time']).groupby(['id'])
        self.model = load_model('test.h5')

    def predict(self):
        ids = []
        for i, df in list(self.df):
            x = df[['adjusted_open']].count
            if x.shape[0] >= 60:
                ids.append([df['id'], df['time']])

        print(ids)
        x_input = np.empty((len(ids), 60, 6), dtype=np.float32)

        current_point = 0

        for i, df in list(self.df):
            df['moving_average'] = df['adjusted_close'].rolling(5).mean()
            x = df[['adjusted_open', 'adjusted_high', 'adjusted_low', 'adjusted_close', 'adjusted_volume', 'moving_average']].values
            if x.shape[0] >= 60:
                x_input[current_point, :, :] = x[-60:, :]
            current_point += 1

        y = model.predict(x_input)
        print(y)
        return y
