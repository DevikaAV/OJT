#  Write a Python program to print the multiplication table of a number using a for loop.
number=int(input("Enter the number:"))
for i in range(1,11):
    print(number , '*', i,'=',number *i)