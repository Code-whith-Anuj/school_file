'''while a program to dispaly if a number entered by usesr is an even number or an odd number '''

# Taking input for the user 
number = int(input("enter odd or even number : "))

# If's find. It's number is odd or even

if (number <= 0):
    print("this is not valid")

elif  (number % 2 == 0):
    print(f"{number} is even number")

else :
    print(f"{ umber} is odd number ")