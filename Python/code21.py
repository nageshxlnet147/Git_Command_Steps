# Loops

# While loop
n = 1
while n<=5:
    print(f"{n}")
    n += 1

# for loop
n = 5
for i in range(n):
    print(f"{i}")

# palindrome logic
n = 147
r = []
while n != 0:
    r.append(n%10)  # n%10 gives the last digit of the given number at every iteration
    n = n // 10     # n//10 it remove the last digit of the given number at every iteration
print(f"{r}")

# Integer to binary conversion
k = 6
b = []
while k!=0:
    r = k%2     # n%2 gives the last digit of the given number at every iteration
    k = k//2    # n//2 it remove the last digit of the given number at every iteration
    b.append(r) 
print(b[::-1])  # reverse the list

