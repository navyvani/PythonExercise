x=input("enter a string")
for i in x:
    if (i.isalpha()):
        print ("{} is an alphabet".format(i))
    elif (i.isdigit()):
        print ("{} is number".format(i))
    elif (i.isnumeric()):
        print ("{} is numeric".format())