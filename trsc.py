import math 
while True:
    print('''What is your choes....
1. triangle 
2. rectangle
3. square 
4. circle 
''')
    num = int(input("enter your choes (1/2/3/4) : "))
    if num <= 0 or num >= 5:
        print('''your choes are not foud 
pleas try agen.....
        ''')
        continue
    elif num == 1:
        print('''what you whant
1. perimeter of a tringle 
2. area of a tringle 
         ''')
        cho = int(input("enter your chois (1/2) : ")) 
        if cho <= 0 or cho >= 3:
            print("this is not valid ")
            print("try agen.... ")
            continue
        elif cho == 1:
            while True:
                a = int(input("enter side of 'a' : "))
                if a <= 0:
                    print("this is not valid ")
                    print('''try agen.... 
                    ''')
                    break
                b = int(input("enter side of 'b' :" ))
                if b <= 0:
                    print("this is not valid ")
                    print('''try agen.... 
                    ''')
                    break
                c = int(input("enter side of 'c' :" ))
                if c <= 0:
                    print("this is not valid ")
                    print('''try agen.... 
                    ''')
                    break  
                abc = a + b + c
                print(f"Perimerter of a triangle = {abc} ")
                break
        else :
            while True :
                b = int(input("enter 'b' of a triangle : "))
                if b <= 0:
                    print("this is not valid ")
                    print('''try agen.... 
                    ''')
                    break
                h  =   int(input("enter 'h' of a triangle : ")) 
                if h <= 0:
                    print("this is not valid ")
                    print('''try agen.... 
                    ''')
                    break
                area = 0.5 * b * h
                print(f"area of a triangle = {area}")
                break
    elif num == 2 :
        while True:
            print('''enter your choes 
1. Perimeer of a rectangle 
2. area of a rectangle 
 
enter 0 to exset
                       ''')
            g = int(input("Enter your chois(1/2) : "))
            if g <= 0 or g >= 3:
                print("this is not valid ")
                print("try agen.... ")
                break
            elif g == 1 or g == 2 :
                while True:     
                    if g == 1:
                        l = int(input("enter 'l' of a rectangle : "))
                        if l <= 0:
                            print('''this is not vaild 
pleas try agen....
                                ''')
                            break
                        w = int(input("enter 'w' of a rectangle : "))
                        if w <= 0:
                            print('''this is not vaild 
pleas try agen....
                                ''')
                            break
                        p = 2 * (l + w)
                        print(f"Perimeter of a rectangle = {p}")
                        break
                                      
                    else:
                        l = int(input("enter 'l' of a rectangle : "))
                        if l <= 0:
                            print('''this is not vaild 
pleas try agen....
                                ''')
                            break
                        w = int(input("enter 'w' of a rectangle : "))
                        if w <= 0:
                            print('''this is not vaild 
pleas try agen....
                                ''')
                            break
                        a = l * w
                        print(f"Perimeter of a rectangle = {a}")
                        break
    elif num == 3:
        while True:
            print('''Enter you choose
1. perimeter of a square
2. area  of a square

exact to enter "0''   
  ''')      
            o = int(input("enter a you choose (1/2)"))
            if o == 1:
                 a = int(input ("enter 'a' of a square : "))
                 if a <= 0:
                     print('''this is not vaild 
pleas try agen....
                 ''')
                     break
                 A = a ** 2
                 print (f"perimeter of a square = {A} ")
                 break
            elif o == 2:
                a =  int(input("enter 'a' of a square : "))
                if  a <= 0:
                     print('''this is not vaild 
pleas try agen....
                 ''')
                     break
                A = a * 4
                print (f"area of a square = {A} ")
                break
            else:
                print("this is not valid ")
                print("please. try again....")
                print()
                break
    else :
        while True:
            print('''enter your choose :- 
1. Perimeter of a circle
2.  area of circle 

exact to enter '0' ''')
            m = int(input("enter your choose (1/2) : "))
            if m <= 0 or m >= 3:
                print("this is not valid \nplease try agen... \n")
            elif m == 1:
                r = int(input("enter 'r' of a circle : "))
                if r <= 0 :
                    print("this is not vaid \nplease try agen.... \n  ")
                    break
                A = math.pi * r ** 2
                print(f"Perimeter of a circle = {A}")
                break
            else :
                while True:
                    r = int(input("enter 'r' of a circle : "))
                    if r <= 0:
                        print("this is not valid \nplease try agen .... \n")
                        break
                    else:
                        m1 = 2 * math.pi * r 
                        print(f"area of a circle = {m1}")