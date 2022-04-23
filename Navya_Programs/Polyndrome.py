a=int(input("enter a number"))
n=a
res=0
while(n!=0):
    temp=n%10
    res=res*10+temp
    n=n//10
if(a==res):
    print("number is a polyndrome")
else:
    print("number is not a polyndrome")