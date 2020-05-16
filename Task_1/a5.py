'''5. 	Write a program to complete the task given below:
Ask user to enter any 2 numbers in between 1-10 and add both of them to another variable  call z.
Use z for adding 30 into it and print the final result by using variable result.
'''
#--------------------way 1---------------------------------------------

a = int(input("Enter any two number between 1 and 10\n"))
b = int(input("Enter any two number between 1 and 10\n"))
z = a + b
z = z + 30
print(z)
print(type(z))

#--------------------way 2---------------------------------------------

a, b= input("Enter any two number between 1 and 10\n").split()
z = int(a)+ int(b)
z = z + 30
print(z)
print(type(z))

#-------------------way 3-----------------------------------------------

z = 0
mylist = list(map(int, input("Enter any two number between 1 and 10\n").split())) 
for i in range(0,2):
    z = z + mylist[i]
z = z + 30
print(z)




