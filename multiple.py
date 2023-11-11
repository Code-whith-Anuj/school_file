while True:
    try:
        num1 = int(input("Enter a number : "))
        num2 = int(input("Enter to you want to multiple : "))
        if num1 != 0:
            for i in range(1,num2):
                mun = i * num1
                print(mun)
        else:
             print('''Enter  you number = 0 
please try again ...

1. Yes
2. No                      ''')
             m = int(input())
             if m == 1:
                 continue
             else:
                 break                    
    except :
        print ('this is not valid')
        