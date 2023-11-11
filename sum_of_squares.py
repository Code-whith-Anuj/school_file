'''Write a program to find the sum of squares of te firt 100 numbers'''

#Initiaze a variable o store the sum

sum_of_squares = 0
#loop through the fist 100 numer number 
for i in range(1,101):
    sum_of_squares += i ** 2
    
print('this sum of squares of the first 100 natural number is : ',sum_of_squares)    