# Fibonocci series below a number

def fibo(a, b):
    print(a+b),  #
    if a < 100:
        # print(a+b),
        a, b = b, a+b
        fibo(a, b)
    return
print(0),
print(1),
fibo(0, 1)

#Fibanocci series of 10 numbers

def fibonacci(n, a, b):
    if n-1 == 0:
        return a
    else:
        a, b = b, a+b
        print(fibonacci(n-1, a, b))
    return a

fibonacci(10, 0, 1)