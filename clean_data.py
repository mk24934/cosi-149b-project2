import pandas as pd


# Import data
df = pd.read_csv('training_project2.csv')

# Drop date variable
df = df.drop(columns=['open', 'high', 'low', 'close', 'volume', 'dividend', 'split'])

# Split data by IDs and write to different files
dfs = dict(tuple(df.groupby('id')))
list_df = [dfs[x] for x in dfs]
for index, df in enumerate(list_df):
    df['moving_average'] = df['adjusted_close'].rolling(5).mean()
    df.to_csv("data_by_id/" + str(index) + ".csv", index=False)