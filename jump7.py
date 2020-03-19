a=0
while a<101:
    a=a+1
    if a%7==0 or a%10==7 or a%7==10:
        continue
    print(a)
