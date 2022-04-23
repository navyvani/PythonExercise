class learning:
    def __init__(self,username,password):
        print("{} and {}".format(username,password))
        pass
    def m1(self,a,b):
        c=a+b
        return c
    def m2(self,a,b):
        c=a*b
        print("multiplication of {} and {} is {}".format(a,b,c))
        
class student:
    def __init__(self,name,age,marks):
        self._name=name
        self._age=age
        self._marks=marks
    def name_setter(self,name):
        self._name=name
    def age_setter(self,age):
        if (age<self._age):
            pass
        else:
            self._age=age+1
        print(self._age)
    def get_name(self):
        return self._name
sekhar=student('sekhar',30,90)
print(sekhar.get_name())
sekhar.name_setter('Jahnavi')
print(sekhar.get_name())
sekhar.age_setter(1)
        
if __name__ == __main__:
    run()
    s1
    s2
    