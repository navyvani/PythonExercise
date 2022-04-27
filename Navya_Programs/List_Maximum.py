a=int(input("Number of elements="))
l=[]
for i in range(a):
    l1=int(input())
    l.append(l1)
# res=max(l)
# print("maximum number is {}".format(res))
temp=0
for j in l:
    if j>temp:
        temp=j
print("maximum number is {}".format(temp))
