import numpy as np

# Create a 2D NumPy array
array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

# Slicing examples
sliced1 = array[:3, :3]
sliced2 = array[-2:, -2:]
sliced3 = array[::2, ::2]
sliced4 = array[1:4, 1:4]

# Print results
print(sliced1)
print(sliced2)
print(sliced3)
print(sliced4)
