# dataframes is two dimensional which is in a tabular
 

import pandas as pd

#  create adtaframe with a dictionary
data = {
    'name':['devu','devika','dhanya'],
    'Age' :[24,23,24],
    'place':['tvm','kochi','kollam']
}
# convert the data into dataframes
df =pd.DataFrame(data)
# print(df)

# print(df [['name','place']])
# # for accessing each row in the dataframe we need the 
# # inbuilt function in pandas, iloc()
# print(df.iloc[1])

# print(df[df['Age'] > 23])

# add a new column into the dataframe
df['stipend']=[15000,5000,5000]

# remove a column
df=df.drop(columns=['Age'])
print(df)

# statiscal function
# describe() help the summary of statics of your dataframe
print(df.describe())