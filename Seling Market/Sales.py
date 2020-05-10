import pandas as pd
import os
import matplotlib.pyplot as plt

# get all csv file in one list
all_files = []
for file in os.listdir('/home/dalin/Pictures/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data'):
    all_files.append(file)

# create new data frame
all_mouth_data = pd.DataFrame()

# add to all file in one data frame
for file in all_files:
    df = pd.read_csv('/home/dalin/Pictures/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/'+ file)
    all_mouth_data = pd.concat([all_mouth_data,df])

# create new csv in all csv inclue
all_mouth_data.to_csv('all_data.csv', index=False)

# get new csv file
all_df = pd.read_csv('all_data.csv')

# drop all NAN value
all_df = all_df.dropna(how='all')

# create new column get month
all_df['Month'] = all_df['Order Date'].str[0:2]

# dro the non value data
all_df = all_df[all_df['Order Date'].str[0:2] != 'Or']

# month column convert to int type
all_df['Month'] = all_df['Month'].astype('int32')

# Quantity Ordered and Price Each convert to the real type
all_df['Quantity Ordered'] = pd.to_numeric(all_df['Quantity Ordered'])
all_df['Price Each'] = pd.to_numeric(all_df['Price Each'])

# new column sales
all_df['Sales'] = all_df['Quantity Ordered'] * all_df['Price Each']

# group by each month sales
group_month = all_df.groupby('Month').sum()

# Output
#        Quantity Ordered    Price Each         Sales
# Month
# 1                 10903  1.811768e+06  1.822257e+06
# 2                 13449  2.188885e+06  2.202022e+06
# 3                 17005  2.791208e+06  2.807100e+06
# 4                 20558  3.367671e+06  3.390670e+06
# 5                 18667  3.135125e+06  3.152607e+06
# 6                 15253  2.562026e+06  2.577802e+06
# 7                 16072  2.632540e+06  2.647776e+06
# 8                 13448  2.230345e+06  2.244468e+06
# 9                 13109  2.084992e+06  2.097560e+06
# 10                22703  3.715555e+06  3.736727e+06
# 11                19798  3.180601e+06  3.199603e+06
# 12                28114  4.588415e+06  4.613443e+06
# the best sales in month of December it value is nearly 4.613$ mi

#  graph of the month and sales
# month = range(1,13)
# plt.bar(month,group_month['Sales'])
# plt.show()

# Get city from Address and create new column is city
all_df['City'] = all_df['Purchase Address'].apply(lambda x: x.split(',')[1])

# group by city
all_city = all_df.groupby('City').sum()

# Output
#                 Quantity Ordered    Price Each   Month         Sales
# City
#  Atlanta                   16602  2.779908e+06  104794  2.795499e+06
#  Austin                    11153  1.809874e+06   69829  1.819582e+06
#  Boston                    22528  3.637410e+06  141112  3.661642e+06
#  Dallas                    16730  2.752628e+06  104620  2.767975e+06
#  Los Angeles               33289  5.421435e+06  208325  5.452571e+06
#  New York City             27932  4.635371e+06  175741  4.664317e+06
#  Portland                  14053  2.307747e+06   87765  2.320491e+06
#  San Francisco             50239  8.211462e+06  315520  8.262204e+06
#  Seattle                   16553  2.733296e+06  104941  2.747755e+06

# highest sales in San Francisco

# graph
#  graph of the month and sales
# city = all_df['City'].unique()
# plt.bar(city,group_month['Sales'])
# plt.ylabel('Sales')
# plt.xlabel('City')
# plt.show()

# convert to datetime real format
all_df['Order Date'] = pd.to_datetime(all_df['Order Date'])

# create hour column
all_df['Hour'] = all_df['Order Date'].dt.hour

# group by hour
hour = all_df.groupby('Hour').sum()

# output
#       Quantity Ordered  Price Each  Month       Sales
# Hour
# 0                 4428   709296.70  27554   713721.27
# 1                 2619   458490.00  16657   460866.88
# 2                 1398   233833.64   8507   234851.44
# 3                  928   144726.42   5904   145757.89
# 4                  937   162058.18   6148   162661.01
# 5                 1493   229621.21   9301   230679.82
# 6                 2810   445000.11  17539   448113.00
# 7                 4556   740568.11  28850   744854.12
# 8                 7002  1185970.62  43626  1192348.97
# 9                 9816  1628498.49  60981  1639030.58
# 10               12308  1932665.62  76928  1944286.77
# 11               14005  2288855.18  87654  2300610.24
# 12               14202  2299876.68  89161  2316821.34
# 13               13685  2139743.86  85808  2155389.80
# 14               12362  2072194.77  77836  2083672.73
# 15               11391  1931174.99  72060  1941549.60
# 16               11662  1892454.54  72939  1904601.31
# 17               12229  2116777.02  77454  2129361.61
# 18               13802  2207696.93  86421  2219348.30
# 19               14470  2398588.31  91389  2412938.54
# 20               13768  2268185.16  86375  2281716.24
# 21               12244  2030763.83  77103  2042000.86
# 22                9899  1599464.44  62088  1607549.21
# 23                7065  1172625.87  44364  1179304.44

# there for the advertiesment present best time are 11-13 and 19-20

# graph
#  graph of the month and sales
# city = all_df['Hour'].unique()
# plt.bar(city,group_month['Quantity Ordered'])
# plt.ylabel('Quantity Ordered')
# plt.xlabel('Hour')
# plt.show()

# group by product
product = all_df.groupby('Product').sum()

# output
#                             Quantity Ordered  Price Each  ...       Sales    Hour
# Product                                                   ...
# 20in Monitor                            4129   451068.99  ...   454148.71   58764
# 27in 4K Gaming Monitor                  6244  2429637.70  ...  2435097.56   90916
# 27in FHD Monitor                        7550  1125974.93  ...  1132424.50  107540
# 34in Ultrawide Monitor                  6199  2348718.19  ...  2355558.01   89076
# AA Batteries (4-pack)                  27635    79015.68  ...   106118.40  298342
# AAA Batteries (4-pack)                 31017    61716.59  ...    92740.83  297332
# Apple Airpods Headphones               15661  2332350.00  ...  2349150.00  223304
# Bose SoundSport Headphones             13457  1332366.75  ...  1345565.43  192445
# Flatscreen TV                           4819  1440000.00  ...  1445700.00   68815
# Google Phone                            5532  3315000.00  ...  3319200.00   79479
# LG Dryer                                 646   387600.00  ...   387600.00    9326
# LG Washing Machine                       666   399600.00  ...   399600.00    9785
# Lightning Charging Cable               23217   323787.10  ...   347094.15  312529
# Macbook Pro Laptop                      4728  8030800.00  ...  8037600.00   68261
# ThinkPad Laptop                         4130  4127958.72  ...  4129958.70   59746
# USB-C Charging Cable                   23975   261740.85  ...   286501.25  314645
# Vareebadd Phone                         2068   826000.00  ...   827200.00   29472
# Wired Headphones                       20557   226395.18  ...   246478.43  271720
# iPhone                                  6849  4789400.00  ...  4794300.00   98657

# the best product in sale is  AAA Batteries (4-pack)

