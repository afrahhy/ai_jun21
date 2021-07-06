import numpy as np
import pandas as pd

data = {
1:[np.nan,2,np.nan,4,5],
2:[np.nan,2,3,np.nan,5],
3:[np.nan,2,np.nan,4,5],
4:[1,np.nan,3,np.nan,np.nan],
5:[1,2,np.nan,4,5],
6:[1,np.nan,3,np.nan,np.nan],
7:[1,2,3,4,5],
8:[1,np.nan,3,np.nan,np.nan],
9:[1,2,3,4,np.nan],
10:[1,np.nan,3,4,5]}

#exercise 26 
df = pd.DataFrame(data)
(df.isnull().cumsum(axis=1) == 3).idxmax(axis=1)

#exercise 27
df1 = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 
                   'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})
df1.groupby('grps')['vals'].nlargest(3).sum(level=0)