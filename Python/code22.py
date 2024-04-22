
# Functions():

# function  without arguments and without return
def sample():
    n = 2
    print(n)
sample()

# function  without arguments and with return
def sample():
    n = 3
    return(n)
ret = sample()
print(f"{ret}")

# function  with arguments and without return 
def sample(n):
    print(n)
sample(4)

# function  with arguments and with return
def sample(n):
    return(n)
ret = sample(5)
print(f"{ret}")

# function with default arguments
def su(a, b = 0):
    print(f"{a+b}")
su(4, 4)

# function with Variable length arguments or Non-key Variable length arguments
def add(a, b, *c):
    print(f"{a}")
    print(f"{b}")
    print(f"{c}")
add(10, 40, 50)

# function with Variable length arguments or key Variable length arguments
def add(a, b, **c):
    print(f"{a}")
    print(f"{b}")
    print(f"{c}")
add(10, 40, Power = 50)

# functions with packing
def mySum(*args):
    return sum(args)
print(mySum(1, 2, 3, 4, 5))  # Output: 15
print(mySum(10, 20))         # Output: 30

# functions with unpacking
def fun(a, b, c, d):
    print(a, b, c, d)

my_list = [1, 2, 3, 4]
fun(*my_list)  # Output: (1, 2, 3, 4)
# ----------------------------------------------
def fun(a, b, c):
    print(a, b, c)
d = {'a': 2, 'b': 4, 'c': 10}
fun(**d)  # Output: 2 4 10

# Function recursion
def fib(n):
    if n == 0:
        return 1
    return n*fib(n-1)
print(f"{fib(5)}")

# Function recursion depth override
import sys
sys.setrecursionlimit(50)
def fib(n):
    if n == 0:
        return 1
    return n*fib(n-1)
print(f"{fib(40)}")