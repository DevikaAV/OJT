import numpy as np
# split will works in numpy
array=np.array([1,2,3,4,5,6,7,8,9])
split_array =np.split(array, 3)
print("orginal array:",array)
print("splitted array:",split_array)

# multi dimensional
# horizontally and vertically
array_2d =np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
vsplit_array =np.vsplit(array_2d,2)
print("vsplitted array :",vsplit_array)

# horizontally
array_2d =np.array([[1,2,3,9],[4,5,6,7]])
hsplit_array =np.hsplit(array_2d,2)
print("hsplitted array :",hsplit_array)
