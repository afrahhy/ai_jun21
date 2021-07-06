import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.random(size=(5, 3)))
# exercise 23
print(df.sub(df.mean(axis=1), axis=0))

#exercise 24
print(df.sum().idxmin())