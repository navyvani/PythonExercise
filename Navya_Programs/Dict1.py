s='Jahnavi is my princess Jahnavi is my princess Jahnavi is my princess princess princess'
a=s.split()
res={}
for i in a:
    if (i not in res):
        res[i]=1
    else:
        res[i]+=1
print (res)