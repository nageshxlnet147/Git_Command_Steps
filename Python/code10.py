# Bitwise Operator:

# and (&):
a = 5
b = 4
print(a & b)
'''
    101
    110
    ---
    100
    ---
'''

# or (|):
print(a | b)
'''
    101
    110
    ----
    111
    ---
'''

# NOT (~):
print(~b)
'''
    100
    ---
    011
    ---
'''
# XOR (^)
print(a^b)
'''
    101
    110
    ----
    011
    ---
'''

# Left shift (<<)
print(a<<2)

# Right shift (>>)
print(a>>2)