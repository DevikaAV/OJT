# Counts the number of non-zero values in the array
def count_non_zero(array):
    count = 0
    for value in array:
        if value != 0:
            count += 1
    return count

# Example usage:
my_array = [0, 5, 0, 3, 0, 7, 8]
print("Number of non-zero values:", count_non_zero(my_array))
