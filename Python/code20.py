# Conditional statements

# if statement
n = 10
if n==10:
    print(f"{'Yes'}")
else:
    print(f"{'No'}")

# Nested if statement
if n==10:
    print(f"{'Yes'}")
    if n == 9:
        print(f"{'No'}")
else:
    print(f"{'No'}")

# else if statement
if n == 1:
    print(f"{'No'}")
elif n==10:
    print(f"{'Yes'}")
else:
    print(f"{'Yes'}")
