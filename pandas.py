import pandas as pd   
p = pd.Timestamp('2018-12-12 06:25:18')   
do = pd.tseries.offsets.DateOffset(n = 2)   
print(p)   
print(do)  