# Write a Python program to Read/Write to a File 
with open('file.txt', 'w') as file:
    file.write("Hello, this is a sample text.")
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
