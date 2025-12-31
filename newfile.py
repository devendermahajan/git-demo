l=[23,43,54,54,223,1,2,43,54,65,23]
# removing duplicate using loops
u = []
for v in l:
    if v not in u:
        u.append(v)

print("Original list:",l)
print("Unique list:",u)