#A function is a set of instruction of specific task.
#function with No Argument & No Return Value

def printline():
    print("*"*50)

printline()
print("Welcome To user Defined Function Using Python.")
printline()

#function with  Argument & No Return Value

def add(a,b):
    print("Addition :",a+b)

printline()
add=(10,20)
printline()

#function with  Argument & Return Value

def sub(a,b):
    return a-b

printline()
#ans=sub(10,20)
print("Subtration :",sub(10,20))
printline()


