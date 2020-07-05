dic1={1:"john",2:"bob",3:"bill"}
print (dic1)

print(dic1.items())

k=dic1.keys()
for i in k:
    print(i)
    
v=dic1.values()
for i in v:
    print(i)
    
print(dic1[3])

del dic1[2]
print(dic1)