'''
inhertance is a process of creating a new class from exting class.
the Object of one class can aquire the properies of another class is called inhertiance.
'''
class A:
    def getA(self,a):
        self.a=a
    def putA(self,a):
        print("A :",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self,b):
        print("B :",self.b)
class C(B):
    def getC(self,c):
        self.c=c
    def putC(self,c):
        print("C :",self.c)
    
b1=C()
b1.getA(10)
b1.getB(20)
b1.getC(30)
b1.putA(10)
b1.putB(20)
b1.putC(20)


       
