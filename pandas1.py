import pandas as pd

# read csv file
# read xlsx, text(delimite ='/t')
df = pd.read_csv('pandas1.csv')

# first head data
# df.head(6)

# tail data
# df.tail(6)

# columns
# df.columns

# special column
# df[['Name','Type 1']][0:5]

# special column and row
# df['Name'][0:5]

# between row column special location
# df.iloc[1:4]
# df.iloc[1,4]

# all data row by row
# for index, row in df.iterrows():
#    print(index,row['Name'])

# special column and data
# df.loc[df['Type 1'] == 'Fire']

# get mean,max,min,mean, count, 25%, 75%, count, only int.float value
# df.describe()

# get A to Z value
# df.sort_values('Name', ascending=False) #Z-A
# df.sort_values(['Type 1', 'Speed'], ascending=[1, 0])

# adding new  column
# df['Total'] = df['HP']+df['Attack']+df['Defense']

# drop column
# df = df.drop(columns=['Legendary'])

# other way axis 1 meaning horizontal sum
# df['Total'] = df.iloc[:,4:9].sum(axis=1)

# change column position
# cols =list(df.columns)
# df = df[cols[0:1]+[cols[-1]]+cols[1:11]]

# get modified csv,any format
# cols =list(df.columns)
# df = df[cols[0:1]+[cols[-1]]+cols[1:11]]
# df.to_csv('modified.txt', index=False, sep='\t')

# filtering data add & ,| and get new data csv
# new_df = df.loc[(df['Type 1']=='Grass') & (df['Speed']==45) & (df['HP']>30)]
# new_df = new_df.reset_index( drop =True) # rest index and old index out
# def.loc[~df['Name'].str.contains('Mega')] # ~ drop mega

# import re
# new_df = df.loc[df['Name'].str.contains('pi[a-z]*', flags = re.I, regex= True)] # beigan pi use ^

# chang parameters
# df.loc[df['Type 1']=='Fire', 'Type 1'] ='Flemer'
# df.loc[df['Type 1']=='Fire', 'Legendary'] =True

# multiple changes
# df.loc[df['Speed']>60, ['Type 1','Legendary']] = 'new Value'
# df.loc[df['Speed']>60, ['Type 1','Legendary']] = ['new Value','new value2']

# group by
# new_df = df.groupby(['Type 1']).mean().sort_values('HP',ascending=False) # mean(), sum(),count()
# df['count']=1
# new_df = df.groupby(['Type 1', 'Type 2']).count()['count']

# part by limitation dat frame
# for dff in pd.read_csv('pandas1.csv', chunksize=10):
#    print(dff)

















