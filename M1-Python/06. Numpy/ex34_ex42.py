# exercise 34

sol3 = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(sol3)

# exercise 42

sol41 = np.random.random(size=(10,10))
sol42 = np.random.random(size=(10,10))
comparison = np.array_equal(sol41,sol42)
print(comparison)
