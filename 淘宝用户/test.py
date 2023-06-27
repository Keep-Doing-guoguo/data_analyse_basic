import pandas as pd
birthday = '20130311'
a = pd.to_datetime(birthday)
b = a.dt.year


print()
