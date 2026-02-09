#1. Create any two variables and perform the following operations: Addition, Subtraction, Multiplicatio, Division
# a=10
# b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

#2. Take an input from user as a number and check its data type.
# user=input("Enter a num: ")
# print(type(user))

#3. Write a program using conditional statements, where a student can write the exam only if: Attendance is 75% or more, And internal marks are 40 or more
# attendance = int(input("Enter your Attendance: "))
# internal_marks = int(input("Enter your internal marks: "))
# if attendance >= 75 and internal_marks >= 40:
#     print("Eligible to write exam")
# else:
#     print("Not eligible to write exam.")

#4.
# user=float(input("Enter the mobile data used(in GB): "))
# if(user<1):
#     print("Low data usage")
# elif (user>=1 and user<=5):
#     print("Regular User")
# else:
#     print("Heavy User")

#5.	Write a program using conditional statements to find the largest of Four Numbers.
# num1=int(input("Enter the first num: "))
# num2=int(input("Enter the second num: "))
# num3=int(input("Enter the third num: "))
# num4=int(input("Enter the fourth num: "))
# largest=num1
# if num1>largest:
#     largest=num1
# if num2>largest:
#     largest=num2
#     if num3>largest:
#         largest=num3
#         if num4>largest:
#             largest=num4
#             print("The largest number is: ", largest)

#6.	Write a Python program using for loop to print all numbers between 15 and 85 that are divisible by 5.
# for i in range(15,86,5):
#     print(i)
#         OR
# for i in range(15,86):
#     if i%5==0:
#         print(i)

#7.	Write a Python program to print the reverse of a given string using a for loop.
# user=input("Enter the string: ")
# for i in reversed(user):
#     print(i)
#        OR
# user=input("Enter the string: ")
# rev=""
# for i in user:
#     rev=i+rev // takes each chars and pushed backwards by printing the reverse string.
#     print(rev)
#        OR
# a=input("Enter a string: ")
# for i in range(len(a)-1,-1,-1):
#     print(a[i])


# 8.	Write a Python program to print the following pattern:
# *
# **
# ***
# ****
# for i in range(1,5):
#     print("*"*i)

# for i in range(1,5):
#     print(" "*(5-i)," * "*i) 
#      OR
#l=4
# for i in range(1,5):
#     print(" "*l+"* "*i)
#     l=l-1

#Reverse order
# for i in range(4,0,-1):
#     print(" " * (4 - i) + "* " * i)

# n=3
# for i in range(1,n + 1):
#     print(" "*(n - i)+"* "*i)
# for i in range(n - 1, 0, -1):
#     print(" "*(n - i)+"* "*i)

#9.	Write a Python program to print numbers from 1 to N using a while loop. Ask the user to enter a number N and print numbers starting from 1 up to N.
# user=int(input("Enter the number N: "))
# i=1
# while i<=user:
#     print(i)
#     i+=1

#10. Write a Python program to check whether a number is a palindrome using a while loop. 
# num=int(input("Enter a num: "))
# original=num
# reverse=0
# while num>0:
#     digit = num%10
#     reverse=reverse*10+digit
#     num//=10
# if reverse==original:
#      print("Palindrome")
# else:
#     print("Not a Palindrome")