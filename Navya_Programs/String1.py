s='Jahnavi is my princess'
a=s.split()
# print (a)
res=[]
for i in a:
    res.append(i[::-1])
# print (res)
b=' '.join(res)
print (b)