#write a program to find the sum of twe number.
while True:
    
    #creat a list
    list1 = []
    try:
        #defining the two number 
        num1 = int(input("enter a fist number : "))
        num2 = int(input("enter a second number : "))
        
        # add two number in list
        list1.append(num1)
        list1.append(num2)
        
        # Displaying the result
        print(f"{num1} + {num2} =",sum(list1))
    except:
        # Displaying the invalid number
        print("this is not valid")    