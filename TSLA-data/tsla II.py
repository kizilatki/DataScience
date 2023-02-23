# Part two

tesla.head(10)
  # O[1]


# Rolling function provide us to get moving average.
tesla_12_days = tesla['Open'].rolling(window=12).mean()
print(tesla_12_days)
  # O[2]
  

tesla['Volume'].astype("int")
tesla.head(4)
  # O[3]

  
tesla['Adj Close'].astype("int")
tesla.tail(5)
  # O[4]
  
  
big_point = tesla['Open']>= 350
tesla[big_point].head(6)
  # O[5]
  
  
