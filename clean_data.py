import pandas as pd


# Import data
df = pd.read_csv('training_project2.csv')

# Drop date variable
df = df.drop(columns=['open', 'high', 'low', 'close', 'volume', 'dividend', 'split'])

# Split data by IDs and write to different files
unique_ids = df.id.unique()
for id in unique_ids:
    df_new = "df" + str(id)
    exec('{} = df[df["id"] == id]'.format(df_new))
    df_new.to_csv(str(id) + ".csv", sep='\t')
    # df_new['moving_average'] = df['adjusted_close'].rolling(5).mean()