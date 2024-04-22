# set{}
n = {'r','o','o','n','a'}
print(f"{n}")
# or set can be call it as below
m = set(['r','o','o','n','a'])
print(f"{m}")

# set add()
n.add(1)
print(f"{n}")

# set update()
n.update(['n','a','g','e','s','h'])
print(f"{n}")

# set remove()
n.remove('h')
print(f"{n}")

# set difference()
a = {1,2,4,5,6,7}
b = {3,2,5,7,4,9,1}
print(f"{a-b} {a.difference(b)}")

# set intersection()
print(f"{a & b} {a.intersection(b)}")

# set union()
print(f"{a | b} {a.union(b)}")

# set symmetric_difference()
print(f"{a ^ b} {a.symmetric_difference(b)}")