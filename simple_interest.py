'''Whrite a python program to calculate simple iteresrt by inputting thevue of principa maut and ratte 
from the user for a time prio of 5 years.
(HINT: Simple interest = (Principal X Rate X Time)/100) '''

# Taking input from the user 

principal = int(input("enter the princial amount : "))
rate = int(input("enter the Rate of inteest : "))
time = 5 # time perod is 5 years

# Caulating simple interest 

s_i = (principal * rate * time ) / 100

# Displaying the result 

print(f"simple interest : {s_i}")