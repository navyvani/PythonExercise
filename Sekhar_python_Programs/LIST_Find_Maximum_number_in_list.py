# https://www.javatpoint.com/logging-in-python#:~:text=Logging%20is%20a%20Python%20module,when%20they%20work%20to%20logging.
import logging
logging.basicConfig(filename='msg.log', filemode='w', format='%(name)s - %(levelname)s - %(asctime)s -%(message)s')
logger= log =logging.getLogger()
logger.setLevel(logging.DEBUG)

try:
    log.error("reading a number from the console")
    n = int(input("Enter number of elements in the list: "))
    log.info("the red number is {}".format(n))
except  NameError as e:
    print(e)
    print("You should enter an interger value. Rerun the program and enter a number")
    log.error("You should enter an interger value. Rerun the program and enter a number")
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
maximum = l[0]
for i in range(1, len(l)):
    if maximum < l[i]:
        index = i
        maximum = l[i]


print ("Maximum value is %d and it is present at the index %d" % (maximum, index))
print ("Maximum value is {} and it is present at the index {}".format(maximum, index))
