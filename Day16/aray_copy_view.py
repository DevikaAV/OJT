# Check if the returned array is a copy or a view
import numpy as np

# Create a 1-D array with 12 elements
array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshape the array into a 3-D array with the specified dimensions
array_3d = array_1d.reshape(2, 3, 2)

# Print the reshaped array
print(array_3d)

# Check if the reshaped array is a copy or a view
is_view = array_3d.base is not None

# Print whether it's a copy or a view
if is_view:
    print("The reshaped array is a view of the original array.")
else:
    print("The reshaped array is a copy of the original array.")
