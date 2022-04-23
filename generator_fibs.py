def generator_fibanocci(n):
    x=0
    y=1
    yield x
    yield y
    for i in range(2,n+1):
        yield x+y
        x,y = y,x+y
gen_fib=generator_fibanocci(10)
#print (gen_fib)
next(gen_fib)
next(gen_fib)
#for i in gen_fib:
 #   print (i)