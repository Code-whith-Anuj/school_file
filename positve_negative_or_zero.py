'''write a program to chech wheter a number is prositive, negative or zero'''

#Taking input from the user 

num = int(input("enter any number : "))

#Calculating the number is positive, negative or zero 

if (num ==  0 ):
    print(f"{0} is zero")
    
elif (num < 0 ):
    print(f"{num} is negative number ")
    
else :
    print(f"{num} is posiive number ")      