a=int(input("enter a number"))
for i in range(a):
    n=i
    res=0
    while(n!=0):
        temp=n%10
        res=res + temp*temp*temp
        n=n//10
    if(i==res):
        print("{} is an armstrong number".format(i))
	