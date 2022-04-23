d={'a':8,'b':3,'c':10,'d':2,'e':5}
for k in sorted(d,key=lambda k:d[k]):
    print (k,d[k])