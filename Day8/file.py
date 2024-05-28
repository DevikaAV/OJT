import pandas as pd

# read the csv file into dataframe
df=pd.read_csv('pandas.csv',
               dtype={'Age':int, 'Salary':float},
               usecols=['name','Age','Place'])
# read the specific column which we mentioned

print(df)