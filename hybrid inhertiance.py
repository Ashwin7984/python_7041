class A:
    def getA(self,a):
        self.a=a
    def putA(self,a):
        print("A :",self.a)
class B:
    def getB(self,b):
        self.b=b
    def putB(self,b):
        print("B :",self.b)
class C(A,B):
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
