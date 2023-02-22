"""
First of all, we need the relevant libraries. 
Some of the Python libraries are NumPY, Pandas and Matplotlib.
"""

import pandas as pd
from matplotlib import pyplot as plt

# Then, need to import the file (such as "csv" file) successfully. Be careful for typo!
aapl = pd.read_csv("D:\PYTHON\Data Analysis/AAPL.CSV")
appl
# Out[1]


# you can able to set index like this:
apple= aapl.set_index("Date")
apple.head(7)
# Out[2] 
