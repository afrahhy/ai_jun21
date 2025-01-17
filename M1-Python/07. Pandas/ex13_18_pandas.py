import numpy as np
import pandas as pd

# df

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}


df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

# exercise 13
df.loc['f', 'age'] = 1.5

#exercise 18

df.sort_values(by=['age', 'visits'], ascending=[False, True])
print(df)
