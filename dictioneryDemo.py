d={101:"Shivansh",899:"mohit",909:"Ashwin",656:"Yash"}

print(d)
print(d[899])
#print(d["yash"])
print(d.get(909))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop())
print(d)
d.popitem()
print(d)
d1={123:"yash",999:"Ashwin",767:"Priya",565:"Hritik"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])
d[998]={1:"python",2:"Java",3:"Automation",4:"c",5:"c++"}
print(d)
print(999 in d)
print(d[998)]



