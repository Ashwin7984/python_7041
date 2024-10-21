import UDF

while True:
    print("*"*40)
    print("1.OddEven")
    print("2.MaxOfTwo")
    print("3.MaxOfThree")
    print("4.Fibonacci")
    print("5.Prime")
    print("6.Exit")
    print("*"*40)
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        n=int(input("Enter Value:"))
        UDF.OddEven(n)
        print("*"*40)
    elif choice==2:
        n1=int(input("Enter Value:"))
        n2=int(input("Enter Value:"))
        UDF.MaxOfTwo(n1,n2)
        print("*"*40)
    elif choice==3:
        n1=int(input("Enter Value:"))
        n2=int(input("Enter Value:"))
        n3=int(input("Enter Value:"))
        UDF.MaxOfThree(n1,n2,n3)
        print("*"*40)
    elif choice==4:
        n=int(input("Enter Value:"))
        UDF.Fibonacci(n)
        print("*"*40)
    elif choice==5:
        n=int(input("Enter Value:"))
        UDF.Prime(n)
        print("*"*40)
    elif choice==6:
        n=("Thank you For using Our Services.")
        print("*"*40)
        break
    else:
        print("Invalid Choice. Please Try Again.")
        print("*"*40)
