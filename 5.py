#Functions
# Built-in Function

# def fun_day():
#     print("Holiday"+"Good News")
#     print("Travel hours")
#     print("Started with functions")
#     print("lunch break")
#     print("Practice Session")
# fun_day()

# def Marriage():
#     print("Welcome to our Wedding")
#     print("With your blessings")
#     print("Groom Weds Bride")
#     print("Venue: Fuction Hall, Bengaluru")
#     print("Parents Name")
#     print("Date: Not yet fixed")
#     print("Time for lunch")
# Marriage()


#User-defined function
#1. no input no output(no argument and no return value)

# def abc():
#     print("Hello")


# def add():
#     a=10
#     b=20
#     c=a+b
#     print(c)
# add() // if the function is not called there will be no input or output

# x=10                                    
# y=20
# add()
# print(x)
# print(y)

 
#print(a)
#print(b)
#print(c) if u print them it is error because they are local variables
#  and they are not accessible outside the function

#2. with input no output(argument for no return value)

# def add(a,b):
#     print(a+b)
# add(2,3)# assignning input value

# x=10
# y=20
# add(x,y)

#3. with input and output(with agument for return value)
# def add(a,b):
#     return(a+b)
# add(3,4)

# x=10
# y=20
# z=add(x,y)
# print(z)


#4. no input with output(No argument for with return value)

# def add():
#     a=10
#     b=20
#     c=a+b
#     return (c)

# z=add()
# print(z)


def odd_even(num):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")
odd_even(1)