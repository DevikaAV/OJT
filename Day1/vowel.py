
vow = input("Enter a string: ")
count = 0
for i in vow:

    if i in 'aeiouAEIOU':
        count += 1
print("Number of vowels:",count)