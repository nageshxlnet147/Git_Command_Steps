# String representation " ", ' ', """ """, ''' '''. 

#single line comments " ", ' '.
string1 = "Hello World!"
print(string1)
print(type(string1))

string2 = 'Hello World!'
print(string2)
print(type(string2))

#Multi line comments """ """, ''' '''.
string3 = """Hello
World!
"""
print(string3)
print(type(string3))

string4 = '''Hello
World!
''' 
print(string4)
print(type(string4))

#String to converstions

#String to string conversion
string= str(string1)
print(string)
print(type(string))

#String to set conversion
set1 = set(string1)
print(set1)
print(type(set1))

#String to list conversion
lst1 = list(string1)
print(lst1)
print(type(lst1))

#String to tuple conversion
tpl1= tuple(string1)
print(tpl1)
print(type(tpl1))
