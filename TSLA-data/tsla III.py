"""
need to import Matplotlib library for the "data visualization".
data visualization is essential and sensible as good as data explanations.
"""

from matplotlib import pyplot as plt

tesla['Close'].plot()                 # you can select only one index and use "show" to view graph.
plt.show()
  # Out[1]
  

#Let's elaborate:
tesla = pd.read_csv("D:\PYTHON\Data Analysis/TSLA.csv", index_col='Date', parse_dates=True)
tesla['Close'].plot(title= 'Tesla')
plt.ylabel('Closed Price')
plt.show()
  # Out[2]
  
  
# graphics with the between specific two dates and particular index.
tesla.loc['2022-01-01' : '2022-03-31', 'Close'].plot(title='A Special Graph for Tesla')
plt.show()
  # Out[3]
  
  

  
