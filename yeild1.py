def topten():
    while n<=10:
        sq=n*n
        yield sq
        n += 1
values=topten()
for i in values:
    print(i) 