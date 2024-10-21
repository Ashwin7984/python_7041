def Square():
    try:
        x=int(input("Enter X :"))
        if x>0:
            print("Square Of ",x,"Is : ",x*x)
        else:
            raise Exception
    except Exception as e:
            print("Please Enter Positive Values Only.Try Again")
            Square()
Square()
