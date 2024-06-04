#  How to inverse a matrix using NumPy
import numpy as np

# Create an example 3x3 matrix
matrix = np.array([[1, 2, 3], 
                   [0, 1, 4], 
                   [5, 6, 0]])

# Calculate the inverse of the matrix
inverse_matrix = np.linalg.inv(matrix)

# Print the inverse matrix
print("Inverse matrix:")
print(inverse_matrix)
