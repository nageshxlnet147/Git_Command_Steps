# String

# Normal string representation

print('Roona', "\nRoona1", '''\nRoona2''', """\nRoona3""")

# f-string representation
print(f"{'Roona4'}")

#str.formate() string representation
print("{}".format("Roona5"))

# String capitalize()
n = 'roona6'
print(f"{n.capitalize()}")

# String title()
m = 'roona anoor'
print(f"{n.title()}")

# String upper()
print(f"{n.upper()}")

# String lower()
print(f"{m.lower()}")

# String isalnum()
print(f"{n.isalnum()} {m.isalnum()}")

# String isalpha()
k = 'Roona'
print(f"{k.isalpha()}")

# String isdigit()
l = '12345'
print(f"{l.isdigit()}")

# String len()
print(f"{len(l)}")

# String endswith()
p = "Roona.tphkf"
print(f"{p.endswith('.tphkf')}")

# String slicing()
print(f"{p[4:8:2]}")