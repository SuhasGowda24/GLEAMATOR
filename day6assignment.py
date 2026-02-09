#1.	Write a Python program using a for loop to print all numbers between 10 and 100 that are divisible by 7.
# for i in range(10,101):
#    if i%7==0:
#     print(i)


#2.	Write a Python program to calculate the factorial of a number using a for loop. Take the number as user input.
# user=int(input("Enter the number: "))
# fact=1
# for i in range(1,user+1):
#     fact=fact*i #5=1*2*3*4*5=120
# print(fact)


#3.	Write a Python program to print the following pattern using a for loop:
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,6):
#     print(str(i)*i)


#4.	Write a Python program to print the following pattern:
#  *****
#   ***
#    *

# for i in range(5,0,-2):
#     print(" " * (5 - i) + "* " * i)


#5.	Write a Python program using a while loop to find the sum of digits of a given number.(Example: 123 → 1 + 2 + 3 = 6)
# num=int(input("Enter digits: "))
# digits=0
# while num>0:
#     digits=digits+(num%10) #Add last digit
#     num=num//10            #Remove last digit
# print(digits)

#6.	Write a Python program using a while loop that keeps asking the user to enter a number until they enter a negative number.
# num=int(input("Enter the number: "))
# while num>=0:
#     num=int(input("Enter the number: "))
# print("Negative number is entered, The loop ends here.")


#7.	Write a Python program using try and except to handle invalid input when the user enters a number. Display a proper error message if the input is not numeric.
# try:
#     num=int(input("Enter a number: "))
#     print("The entered number is:",num)
# except ValueError:
#     print("Please enter the valid number.")
# finally:
#     print("Entered number, The program ends here")


#8.	Write a Python program to divide two numbers entered by the user.Handle the following exceptions:o	Invalid input, o Division by zero
# try:
#     num1=int(input("Enter the first number: "))
#     num2=int(input("Enter the second number: "))
#     result=num1/num2
#     print(result)
# except ValueError:
#     print("Please enter a valid number.")
# except ZeroDivisionError:
#     print("Division by zero is not possible.")
# finally:
#     print("Succesfully executed.")


#9.	Write a Python program that allows a user 3 attempts to enter a correct PIN number.If the PIN is incorrect after 3 attempts, display "Account Locked".(Use loop and conditional statements)
# correct_pin=2004
# attempts=0
# while attempts<3:
#     user_pin=int(input("Enter PIN: "))
#     if user_pin==correct_pin:
#         print("Correct PIN.")
#         break
#     else:
#         print("Incorrect PIN")
#         attempts+=1
# if attempts==3:
#     print("Account Locked")


#10.	Write a Python program using try, except, and finally:
# •	Ask the user to enter a number
# •	If the number is negative, raise a custom error
# •	Handle the error
# •	Finally print "Program Executed"

# try:
#     user=int(input("Enter a number: "))
#     if user<0:
#         raise ValueError("Negative number is entered.") //raise is used to manually generate an exception.
#     print(user)
# except ValueError:
#     print("Invalid Input")
# finally:
#     print("Program Executed")


def emotion_detector():
    user_slept=float(input("Enter the number of hours slept: "))
    if user_slept<5:
        print("Very Angry")
    elif user_slept>=5 and user_slept<=7:
        print("Chill")
    else:
        print("Feeling Good")
emotion_detector() #call the function

