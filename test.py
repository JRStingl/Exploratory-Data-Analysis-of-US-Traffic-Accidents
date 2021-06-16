import pandas as pd

df = pd.read_csv('../data/US_Accidents_Dec20_Updated.csv')

print(df.describe())

print(df.info())

print(df[df['State']=='WI'].count())