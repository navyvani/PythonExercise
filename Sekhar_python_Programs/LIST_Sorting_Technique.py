l = [5,44,3,2,11]
for i in range(len(l) - 1):
    minimum = l[i]
    index = 0
    for j in range(i+1, len(l)):
        if minimum > l[j]:
            minimum = l[j]
            temp = l[i]
            l[i] = minimum
            l[j] = temp
        print l
print (l)
