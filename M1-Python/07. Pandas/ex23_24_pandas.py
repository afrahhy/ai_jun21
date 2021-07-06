df = pd.DataFrame(np.random.random(size=(5, 3)))
# exercise 23
df.sub(df.mean(axis=1), axis=0)

#exercise 24
df.sub(df.mean(axis=1), axis=0)