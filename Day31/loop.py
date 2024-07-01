# python for loop
list=['html','Css','php','java']
print("This is our list ",list)
i=1 
for val in list:
     print("List Item",i,"is",val)
     i=i+1

# for loop with tuple
tuple=('html','Css','Java','mysql','Python') 
print("This is our Tuple ",tuple)
i=1

for val in tuple:
    print("Tuple Item",i,"is",val)
i=i+1

# For loop with string
string="devika" 
for val in string:
     print(val)

# Range Function

for val in range(11):
     print(val)


# For loop with else condition
num = int(input("Enter a Number : "))
for i in range(2,num):
     if(num%i==0): 
        print("%d is not a prime number..."%num)
        break
else: 
        print("%d is a prime number..."%num)

