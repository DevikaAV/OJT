# Write a python program to Delete a file
import os

# Specify the filename
filename = 'file.txt'

# Check if the file exists
if os.path.exists(filename):
    # Delete the file
    os.remove(filename)
    print(f"{filename} has been deleted.")
else:
    print(f"{filename} does not exist.")
