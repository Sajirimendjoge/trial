# Q6. Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is : int/float/string/etc

ans = input("Enter the value")
print("The input value data type is : {}".format(type(ans)))

'''
Have a doubt regarding this. As the input type of all inputs taken by input method will be string, 
all inputs will be same unless we have typecasted the input to int or float.
Even in that case all input values will be same that is the one in which we have typecasted the value. 
so how come we find out the user desired data type?
'''