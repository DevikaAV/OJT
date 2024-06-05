# iterations
import numpy as np
# for-in loop
# 1D array
array1D =np.array([1,2,3,4,5,6])
# iterate the elements in this array
print("array_1D:",array1D)

for elements in array1D:
    print(elements)

# create 2D array
array2D =np.array([[1,2,3],[4,5,6],[7,8,9]])
print("array_2D:",array2D)

# iterate  2D array
# for rows in array2D:
#     # print(elements)
#     print(rows)
#     for elements in rows:
#         print(elements)
# iterate the elements without nested loops
for elements in np.nditer(array2D):
    print(elements)


# iterate the elements with index
for index, elements  in np.ndenumerate(array2D):
    print(f"index : {index},Elements :,{elements}")





