# List overview

value_list = [ 1, 2, 3, 4, 5, 1.2, "python", [1, 2, 3] ]
# List accessing
print(value_list[6])

# List updating
value_list[3] = 'Roona'
print(value_list)

### List operations ###
# Repetition *:
print(value_list * 2)

# List concatenation:
value_list1 = [1, 2, 3, 4, 5, 1.2]
print(value_list+value_list1)

# List length:
print(len(value_list), len(value_list1))

# List Iteration:
for i in value_list1:
    print(i)

# List Membership:
print(5 in value_list, 6 in value_list)

### List Inbuilt Function: ###
# List append():
value_list.append("Nagesh")
print(value_list)

# List Extend():
value_list.extend(["Moon", "Sun"])
print(value_list)

# List copy():
lst1 = [1, 2, 3, 5, 3, 7]
lst2 = lst1
print(lst1, lst2)

lst2.append("6") # here lst2 only we are modified but by default lst1 also modified same as list2.
print(lst2, lst1)

lst2 = lst1.copy() # here copy() create the shadow of the lst1 and assigned to lst2 so once we update the any list it will update the those list enough not for other list.
lst1.append("431")
print(lst1, lst2)
