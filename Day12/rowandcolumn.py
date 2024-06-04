#  Find the number of rows and columns of a given matrix using NumPy
import numpy as np

# Example matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Get the shape of the matrix
rows, columns = matrix.shape

print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")
