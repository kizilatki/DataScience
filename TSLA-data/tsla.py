import pandas as pd

#need to import file:
tesla = pd.read_csv("D:\PYTHON\Data Analysis/TSLA.csv")
tesla.head()
  #Out[1]
  
tesla.index = tesla['Date']
tesla.index.name = 'Date'
tesla.head(3)                #This meant is first 3 row.
  #Out[2]
  
tesla.drop('Date', axis=1, inplace=True)
tesla.head(3)
  #Out[3]


tesla.index
""" output like this:
Index(['2021-12-08', '2021-12-09', '2021-12-10', '2021-12-13', '2021-12-14',
       '2021-12-15', '2021-12-16', '2021-12-17', '2021-12-20', '2021-12-21',
       ...
       '2022-11-23', '2022-11-25', '2022-11-28', '2022-11-29', '2022-11-30',
       '2022-12-01', '2022-12-02', '2022-12-05', '2022-12-06', '2022-12-07'],
      dtype='object', name='Date', length=252) """


# you can search the data with loc or iloc(integer location):
tesla.loc['2022-12-05']
""" output:
Open         1.894400e+02
High         1.912700e+02
Low          1.805500e+02
Close        1.824500e+02
Adj Close    1.824500e+02
Volume       9.312270e+07
Name: 2022-12-05, dtype: float64 """


tesla.loc['2021-12-08' : '2021-12-21']
  #Out[4]
















