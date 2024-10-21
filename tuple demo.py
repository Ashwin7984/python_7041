t=(1,2,"tops",1.1,2.2,[100,200,300],10,20,True,"python",False)

print(t)
print(t.count(1))
print(t.index(10))

for i in t:
    print(i)

print(20 in t)
print(t[5])
t[5].append(400)
print(t)
