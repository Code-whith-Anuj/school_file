#Write a program (WAP) to print the words starting with an alphabet in a user entered string.

string = "hello I an Anuj and this is a test of string"
print(string) 
spl = string.split()
print(spl)
find = input("")

for i in spl:
    if i.startswith(find):
        print(i)