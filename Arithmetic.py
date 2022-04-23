class Arithmetic():
    def __init__(self,a=10,b=10):
        self._a=a
        self._b=b
        self._c=None
    def addition(self):
        k=self._a+self._b
        print(k)
        return k
    def substraction(self,a,b):
        print(a-b)
    def multiplication(self):
        print(self._a*self._b)
    def top_up(self,c):
        #self._c=c
        op=self.addition()+c
        print(op)
        
    
o=Arithmetic(5,6)
o.addition()
o.substraction(10,4)
o.multiplication()
o.top_up(8)