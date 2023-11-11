'''A student has to travel a distance of 450 km by car at a certain 
Speed waite program to find the total time taken to cover the distance.'''

#Taking input from the user 

distansce = 450 #distansce in kilometer 
speed = int(input("enter the average speed in km/h : ")) #speed in km/h

#fungtian to catcalate time 

time = distansce / speed 

#Displaying the result

print(f"Tata time taken to cover {distansce} km at {speed} km/h is {time} hours")