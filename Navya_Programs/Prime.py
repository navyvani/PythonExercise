a=int(input("enter a number"))

if(a<2):
    print("please enter a number greater than 2")
for n in range(2,a):
    factor=0
    for i in range(2,n):
        if(n%i==0):
            factor=1
        # print(a,i)
            break
    if(factor==0):
        print("{}".format(n),)
        
        
 

    
    
