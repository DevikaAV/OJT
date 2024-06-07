#   Convert the following 1-D array with 12 elements into a 2-D array. The outermost dimension will have 4 arrays, each with 3 elements:
import numpy as np

# Create a 1-D array with 12 elements
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape the array into a 2-D array with 4 arrays, each with 3 elements
array_2d = array_1d.reshape(4, 3)

# Print the reshaped array
print(array_2d)
