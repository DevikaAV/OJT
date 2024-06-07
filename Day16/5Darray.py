#   Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4
import numpy as np

# Create a vector with values 1, 2, 3, 4 and set ndmin to 5
array = np.array([1, 2, 3, 4], ndmin=5)

# Print the shape of the array to verify its dimensions
print("Shape of the array:", array.shape)

# Verify that the last dimension has the value 4
print("Last dimension value:", array.shape[-1])

