#  Write a Python program that reads a file and prints its content.
#  Handle ‘FileNotFoundError’ and ‘PermissionError’ exceptions.
filename = 'file.txt'  
try:
    print(open(filename, 'r').read())
except FileNotFoundError:
    print(f"The file '{filename}' was not found.")
except PermissionError:
    print(f"Permission denied when trying to read the file '{filename}'.")
