# no input no output

def add():
    a=10
    b=20
    c=a+b
    print(c)

x=10
y=20
add()
print(x)
print(y)

 
#print(a)
#print(b)
#print(c) if u print them it is error because they are local variables
#  and they are not accessible outside the function

print("--------------------------------------------------")
# with input no output

def add(a,b):
    c=a+b
    print(c)

x=10
y=20
add(x,y)
print("--------------------------------------------------")
# no input with output
def add():
    a=10
    b=20
    c=a+b
    return c


z=add()
print(z)
print("--------------------------------------------------")

# with input and output
def add(a,b):
    c=a+b
    return c

x=10
y=20
z=add(x,y)
print(z)
print("--------------------------------------------------")