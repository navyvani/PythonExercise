try:
    n = int(input("Enter number of elements in the list: "))
except  NameError as e:
    print(e)
    print("You should enter an interger value. Rerun the program and enter a number")
    exit(0)
l = []
for i in range(n):
    try:
        l.append(int(input("Enter a number to append to list: ")))
    except NameError:
        l.append(int(input("Enter Non integer value. Enter integer value to append to list:")))

print("Entered list of values are {}".format(l))

# max = None
index = 0
minimum = l[0]
for i in range(1, len(l)):
    if minimum > l[i]:
        index = i
        minimum = l[i]

print ("minimum value is %d and it is present at the index %d" % (minimum, index))
print ("minimum value is {} and it is present at the index {}".format(minimum, index))

# Moving smallest number to first index
temp = l[0]
l[0] = minimum
l[index] = temp