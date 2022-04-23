d={'a':8,'b':3,'c':10,'d':2,'e':5}
for k in sorted(d.items(), key=lambda k:k[1]):
    print (k)