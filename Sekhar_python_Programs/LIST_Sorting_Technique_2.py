# Bubble Sort
# https://www.geeksforgeeks.org/bubble-sort/

l = [5,44,3,2,11]
for i in range(len(l) - 1):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print (l)
