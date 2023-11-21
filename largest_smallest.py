#Write a program (WAP) to find the largest and smallest number in a list.

def find(num):
    print(num)
    #lagest number
    a = max(num)
    #Smallest number
    b = min(num)
    print(f"'{a}' is largest number and '{b}' is smallest number")

list1 = [12,32,543,65,234,52,23,1,34,4,5]
find(list1)