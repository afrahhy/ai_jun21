# exercise 13
sol1 = np.random.random(size=(10,10))
print(np.min(sol1), np.max(sol1))

# exercise 15

sol2 = np.ones((5,5))
sol2[1:-1, 1:-1] = 0

print(sol2)