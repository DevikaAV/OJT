#  Print the value of the base attribute to check if an array owns it's data or not

import numpy as np

# Original array
original_array = np.array([1, 2, 3, 4, 5])

# Make a view of the original array
view_array = original_array.view()

# Check if view_array owns its data
print("View array base:", view_array.base)
