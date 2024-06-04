#  Calculate the sum of the diagonal elements of a NumPy array 3*3 and 4*4
import numpy as np

# Create the matrices
matrix_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_4x4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# Calculate the sum of the diagonal elements
sum_diagonal_3x3 = np.sum(np.diagonal(matrix_3x3))
sum_diagonal_4x4 = np.sum(np.diagonal(matrix_4x4))

# Output the results
print(f"Sum of diagonal elements of 3x3 matrix: {sum_diagonal_3x3}")
print(f"Sum of diagonal elements of 4x4 matrix: {sum_diagonal_4x4}")
