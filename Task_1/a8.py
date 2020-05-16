# Q.8 If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?


#Answer = Yes

#demo:

a = 7 
print(type(a))
#output = <class 'int'>
a = 2.5
print(type(a))
#output = <class 'float'>

#Reason:
'''
Because Python is a dymanic language where variables can be reinitialiosed again and again. 
The data type of the variables is not static.
'''