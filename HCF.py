def cal_HCF(a,b):
    for i in range(1,a + 1):
        if (a % i == 0 and b % i == 0 ):
            HCF = i
    return HCF
    
    
a = int(input("enter fast number : "))    
b = int(input("enter second number : "))

if a < b:
    HCF = cal_HCF(b,a)
    print(HCF)
    
else :
    HCF = cal_HCF(a,b)
    print(HCF)    