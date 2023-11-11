list1 = list("aeiouAEIOU")
name = input("Enter your name: ")

name1 = list(name)

line = len(name)

sum = 0

for i in range(line):
    if name1[i] in list1:
        sum += 1

print(sum)