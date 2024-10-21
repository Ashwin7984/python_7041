def OddEven(n):
    if n%2==0:
        print(n,"Is Even")
    else:
        print(n,"Is odd")

def MaxOfTwo(a,b):
    if a>b:
        print(a,"Is Max")
    else:
        print(b,"Is Max")
def MaxOfThree(a,b,c):
    if a>b:
        if a>c:
            print(a,"Is Max")
        else:
            print(c,"Is Max")
    elif b>c:
        print(b,"Is max")
    else:
        print(c,"Is Max")
def Fibonacci(n):
    a,b=0,1
    print(a,end=" ")
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()
def prime(n):
    if n%2!=0:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print(n,"Is Not Prime")
                break
        else:
            print(n,"Is prime")
    else:
        print(n,"Is Not Prime")
        



                    

               
        
        
