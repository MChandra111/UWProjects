#!/usr/bin/env python3

#Dictionaries 1
d = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
print(d)
d.popitem()
print(d)
d['fruit'] = 'Mango'
print(d)
print(d.keys())
print(d.values())
print("cake" in d)
print("Mango" in d.values())


#Dictionaries 2
d = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
d_copy = {}
d_copy['name'] = d['name'].lower().count()
d_copy['city'] = d['city'].lower().count()
d_copy['cake'] = d['cake'].lower().count()

#Sets
s2 = set()
s3 = set()
s4 = set()
for i in range(20):
    if i % 2 == 0:
        s2.update([i])
for i in range(20):
    if i % 3 == 0:
        s3.update([i])
for i in range(20):
    if i % 4 == 0:
        s4.update([i])

print(s2)
print(s3)
print(s4)
print(s3.issubset(s2))
print(s4.issubset(s2))

#Sets 2
s = set()
for i in "python":
    s.update([i])
s.update(['i'])

fs = frozenset(('m', 'a', 'r', 'a', 't', 'h', 'o', 'n'))
print(s.union(fs))
print(s.intersection(fs))
