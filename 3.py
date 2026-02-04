#Conditional Statement

#If-elif-else Condition
marks = int(input("Enter your marks: "))
if marks>=90:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=50:
    print("Grade C")
elif marks>=35:
    print("Pass")
if marks:
    print("Please Enter your marks")



#If-else Condition
# age=16
# if age>17:
#     print("Eligible for vote")
# else:
#     print("Not Eligible for vote")

#If Condition
# age=18
# if age>=18:
#     print("Eligible for vote")


#Explicit Conversions
# print(bool("Hello"))
# print(bool(5)) //True if the number exceeds 1 or not empty
# print(bool(" ")) //True because of spacing 
# print(bool("")) //False no space

#Concatination
# age=str(21)
# print("My age is " + age)


# v=2+3j
# w="-1+(-2)"
# x=v+w  //TypeError: unsupported operand type(s) for +: 'complex' and 'str'
# print(x)

# t="Error"
# a=str(24)
# c=t+a
# print(c)

# t="Error"
# a=24
# c=t*a //If multiplied t with a then error is printed 24 times
# print(c)

# y="hello"
# z="Bye"
# c=y+z //helloBye
# print(c)


# a="10.5"
# b=-101
# c=a-b #TypeError: unsupported operand type(s) for -: 'str' and 'int'
# print(c)
# print(5*"a")#5mult with a 5times
# print(5*"5")#5 will be multipled with 5(5times)
# print("5"+"5")


# x="100"
# a="2"
# b=int(x) #Converts Str->Int
# c=int(a)
# print(b)
# print(c)
# print(type(b),type(c))


# x="100"
# a=2
# b=int(x) #Converts Str->Int
# print(b)
# print(type(b))
# c=b+a
# print(c)
# print(type(c))



#Implicit Conversions
# a=5
# b="5"
# c=a+b
# print(c)
# print(type(c))

#Complex with Boolean

# a=True
# b=5+10j
# c=a+b
# print(c)
# print(type(c))


# a=False
# b=10
# c=a/b
# print(c)
# print(type(c))

# a=True
# b=2
# c=a/b
# print(c)
# print(type(c))

# a=True
# b=2
# c=a*b
# print(c)
# print(type(c))

# a=False //False=0
# b=2
# c=a+b
# print(c)
# print(type(c))

# a=True //True=1
# b=2
# c=a+b
# print(c)
# print(type(c))

#Negative

# a=2.2
# b=-5
# c=a*b
# print(c) //float 
# print(type(c))

#Complex

# a=5
# b=4+3j
# c=a*b
# print(c)
# print(type(c))

# a=5
# b=4+3j
# c=a+b
# print(c)
# print(type(c))

# a=2.5
# b=5
# c=a+b 
# print(c)
# print(type(c))


# a=5
# b=2.5
# c=a+b 
# print(c)
# print(type(c))