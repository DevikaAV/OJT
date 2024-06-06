# Make a view, change the view, and display both arrays
import numpy as np

# Original array
original_array = np.array([1, 2, 3, 4, 5])

# Make a view of the original array
view_array = original_array.view()

# Change multiple elements in the view array
view_array[0] = 99
view_array[2] = 77

# Display both arrays
print("Original array:", original_array)
print("View array:", view_array)
