while True:
    try:
        n = int(input("Enter a number : "))
        if n ==  2  :
            print(f"It is prime number {n}")
            print()
        elif 0 >= n :
            print('''this is not veld 
try again .....
           ''')
        elif 1 < n:
            for i in range(2,n):
                if n % i == 0:
                    print(f"It is not prime number  {n}")
                    print()
                    break
            else :
                print (f"It is prime number {n}")
                print()
    except :
        print ('''this number is not veld
try agen.....
         ''')   