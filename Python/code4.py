# Dictionary The data is stored as key-value pairs.

dict1 = { 
    'name':'nagesh',
    'id':5120
}
print(dict1)
print(type(dict1))

#Dictionary to converstions

#Dictionary to string conversion
string= str(dict1)
print(string)
print(type(string))
# Output: {'name': 'nagesh', 'id': 5120}

#Dictionary to set conversion
set1 = set(dict1)
print(set1)
print(type(set1))
# Output: {'id', 'name'}

#Dictionary to list conversion
lst1 = list(dict1)
print(lst1)
print(type(lst1))
# Output: {'id', 'name'}
