a=[1,2,1,2,2,3,1,1,3,1,2,4,4,2,1,4,2]
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for k,v in d.items():
    if (d[k]>1):
        print ("{} is present {} times".format(k,v))