a=int(input("enter a number"))
n=a
res=0
while(n!=0):
    temp=n%10
    res=res + temp*temp*temp
    n=n//10
if(a==res):
    print("{} is an armstrong number".format(a))