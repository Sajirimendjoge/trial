#Swap two numbers using third variable as result name and do the same task without using any third variable.

a , b = 5, 10
print(a, b)
#with a temp variable
result = a
a = b
b = result  
print(a, b)
#---------------------------------------
#without temp varible 
a , b = b , a
print(a, b)

