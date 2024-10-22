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
class C(A):
    def getC(self,c):
        self.c=c
    def putC(self,c):
        print("C :",self.c)
class D(A):
    def getD(self,d):
        self.d=d
    def putD(self,d):
        print("D :",self.d)
b1=B()
c1=C()
d1=D()
b1.getA(10)
b1.getB(20)
c1.getC(30)
d1.getD(40)

b1.putA()
b1.putB()
b1.putC()
b1.putD()

