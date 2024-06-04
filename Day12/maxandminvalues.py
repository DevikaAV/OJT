# Get the maximum and minimum value from given matrix
import numpy as np

# Define an example matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Find the maximum and minimum values
max_value = np.max(matrix)
min_value = np.min(matrix)

# Print the results
print("Maximum value in the matrix:", max_value)
print("Minimum value in the matrix:", min_value)
