a=0
b=1
n=int(input("enter a number"))
while(b<n):
    b,a=a+b, b
    print (b)
    # 0,1,1,2,3,5,8
    
    # a=0, b=1
    # b=1, a=1
    # b=2, a=1
    # b=3, a=2
    