# List : its an hetrogenious (hetro: multiple, genious: types), but we can change the values once assigned also.
lst1 = [1, 3, 5, 'nagesh', 'roona', 'n', 'r', 1.2, 1.3, 1.4]
print(lst1)
print(type(lst1))

#inserting values in the already defined postion
lst1[2] = 6
print(lst1)

#list to converstions

#list to string conversion
string= str(lst1)
print(string)
print(type(string))

#list to set conversion
set1 = set(lst1)
print(set1)
print(type(set1))

#list to touple conversion
tuple1 = tuple(lst1)
print(tuple1)
print(type(tuple1))
