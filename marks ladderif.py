rno=int(input("Enter rno"))
sname=(input("Enter student name"))
s1=int(input("Enter mark of subject 1:"))
s2=int(input("Enter mark of subject 2:"))
s3=int(input("Enter mark of subject 3:"))

total=s1+s2+s3
per=total/3

print("Roll no",rno)
print("student name",sname)
print("Total",total)
print("percentage",per)

if per>=70:
       print("Distinction")
elif per>=60:
    print("first class")
elif per>=50:
    print("second class")
elif per>=40:
    print("pass")
else:
    print("fail")
