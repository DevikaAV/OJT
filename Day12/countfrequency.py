# How to count the frequency of unique values in NumPy array?
import numpy as np

# Example array
arr = np.array([1, 2, 3, 4, 1, 2, 1, 2, 3, 4, 5])

# Count the frequency of unique values
unique_values, counts = np.unique(arr, return_counts=True)

# Print the unique values and their frequencies
print("Unique values:", unique_values)
print("Frequencies:", counts)
