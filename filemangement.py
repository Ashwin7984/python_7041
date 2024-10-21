
file=open("tops1.txt","w")
file.write("This is file management demo using python.")
file.close()
print("file Written Successfully")
print("*********************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*********************")


file=open("tops1.txt","a")
file.write("\nThis is file now append.")
file.close()
print("*********************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*********************")

file=open("tops2.txt","w+")
file.write("This is w+ mode using python file management .")
print("file current position : ",file.tell())
file.seek(0)
print("file Data :",file.read())
file.close()
print("*********************")


