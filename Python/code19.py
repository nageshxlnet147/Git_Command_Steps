# Dictionary{:}
employee_data = {
    'Name' : 'Roona',
    'Id' : 5120,
    'Company' : 'Accenture',
    'Work': 'AWS'
    }
print(f"{employee_data}")

# Dictionary values accessing through keys
print(f"{employee_data['Name']} {employee_data['Company']}")

# Dictionary values modify by accessing keys
employee_data['Company'] = 'Accenture & Wipro'
print(f"{employee_data}")

# Dictionary values accessing through get() function
print(f"{employee_data.get('Company', 'Accenture')}")

# Dictionary keys accessing
print(f"{employee_data.keys()}")

# Dictionary values accessing
print(f"{employee_data.values()}")

# Dictionary date clear()
print(f"{employee_data.clear()}")