
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


