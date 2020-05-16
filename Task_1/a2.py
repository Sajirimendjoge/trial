#Create a variable of value type complex and swap it with another variable whose value is an integer.

a , b = 4+2j , 4
print(a, b)
#with a temp variable
c = a
a = b
b = c  
print(a, b)
#---------------------------------------
#without temp varible 
a , b = b , a
print(a, b)

