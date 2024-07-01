# For loop with else condition
num = int(input("Enter a Number : "))
for i in range(2,num):
     if(num%i==0): 
        print("%d is not a prime number..."%num)
        break
else: 
        print("%d is a prime number..."%num)

# Nested Loop
# Define the size of the pattern
size = 7

# Nested loops to iterate through rows and columns
for row in range(size):
    for col in range(size):
        # Conditions to determine whether to print '*' or ' '
        if (col == 1 or col == 5) and row != 0:
            print("*", end="")
        elif (row == 0 or row == 3) and (1 < col < 5):
            print("*", end="")
        else:
            print(" ", end="")
    
    # Move to the next line after each row is printed
    print()

    # example 2

    # Initialize an empty string to store the result
result = ""

# Outer loop for rows
for row in range(7):
    # Inner loop for columns
    for col in range(7):
        # Conditions to determine whether to add '*' or ' ' to the string
        if (col == 1 or 
           ((row == 0 or row == 3 or row == 6) and (col > 1 and col < 5)) or 
           (col == 5 and (row != 0 and row != 3 and row != 6))):
            result += "*"
        else:
            result += " "
    
    # Add a newline character after each row is completed
    result += "\n"

# Print the final result
print(result)


