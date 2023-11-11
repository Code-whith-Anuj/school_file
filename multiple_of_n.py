'''write a program to print the fist 'n' multiples of a give number '''

#Get user input for the number and 'n'

number = int(input("enter the number : "))
n = int(input("enter the value of 'n' : "))

# creat a loop to calculate and print multiples

for i in range(1,n+1):
    multiple = number * i #calculate the muliple 
    print(f"{number} X {i} = {multiple}")