global a
a = 10

# both local and global error
# def m1(a):
#     print("value of a inside function m1 is {}".format(a))
#     # global a
#     a = 12
#
#     print("value of a after modification in function m1 is {}".format(a))


def m2():
    print("value of a inside function m1 is {}".format(a))
    global a
    a = 12
    print("value of a after modification in function m1 is {}".format(a))


print("value of a outside function bfere calling m1 is  {}".format(a))
# m1(a)
m2()
print("value of a outside function is  {}".format(a))


# Refer Below Link for understanding global
# https://www.w3schools.com/python/python_variables_global.asp