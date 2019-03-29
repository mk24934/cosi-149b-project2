import pandas as pd


# Import data
df = pd.read_csv('training_project2.csv')

# Drop date variable
data = df.drop(columns=['open', 'high', 'low', 'close', 'volume', 'dividend', 'split'])

data['moving_average'] = data['adjusted_close'].rolling(5).mean()

# Split data by IDs and write to different files
last_row = df.tail(1)
last_id = last_row['id']
print(last_id)
# for index, row in df.iterrows():
