s={10,20,30,"XYZ"}
print(s)
print(type(s))

s.update([88,99])
print(s)

#s.remove(30)
print(s)

f=frozenset(s)