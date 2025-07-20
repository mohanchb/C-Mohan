n=int(input("enter the number"))
p=1
for i in range(1,n+1,1):
    if i%2!=0:
        if(i==1):
            print(p,end="")
        else:
            print(",",end="")
            print(p,end="")
        p+=2
    else:
        if i!=n:
        
            if(i==1):
                print(p,end="")
            else:
                print(",",end="")
                print(p,end="")
            p+=2


