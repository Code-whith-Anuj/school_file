'''Write a program to cheak if a peson is eligible to vote'''

while True: # mack a while loop
    try: # cheak this is valid or not 
        name = input("enter your name : ") #enter her/his name 
        age = int(input(f"{name} enter your age : "))#enter her/his age
        
        #calculating the age 
        
        if age <=0 or age >= 100:
            print(f"{age} is not valid ")
        
        elif age <= 17 :
            print("your are not eigble to vote",name)        
            
        else :
            print(f"your are eigle to vote {name}" )
    except:
        print("this is not valid ")