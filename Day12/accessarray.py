import numpy as np
# create an array
array_2D =np.array(
    [
        # 2*3
    [1,2,3],
     [4,5,6]  
     ]
     )


# accessing a single element
element =array_2D[1,2]
print("element at the index of [1,2]" ,element)
# accessing a single element
element =array_2D[0,1]
print("element at the index of [0,1]" ,element)

# access by row
row =array_2D[1:]
print("the second row will be ",row)
# : symbol refer to entire rows
row =array_2D[0,:]
print("the first row will be ",row)

# access by 2 column
col=array_2D[:, 1]
print("the second column will be ",col)
# slicing
# access the subaeeay wuith row of o and 1,column of 1 ans2
slice_array=array_2D[0:2,1:3]
print("subarrayv:",slice_array)

