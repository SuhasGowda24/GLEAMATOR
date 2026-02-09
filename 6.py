#      Exception Handling

#Try  
# num= int(input("Enter a number: "))
# print(2/num)
# print(-2/num)


# try:
#     num=int(input("Enter a number: "))
#     print(2/num)
#     print(-2/num)



#Except
# try:
#     num=int(input("Enter a number: "))
#     print(2/num)
# except ZeroDivisionError:
#         print("Cannot divide by zero")


#Finally
# try:
#     num=int(input("Enter a number: "))
#     print(2/num)
# except ZeroDivisionError:
#         print("Cannot divide by zero")
# finally:
#       print("Execution COmpleted")


# try:
#     num=int(input("Enter a number: "))
#     print(2/num)
# except ZeroDivisionError:
#         print("Cannot be divide by zero")
# except ValueError:
#       print("Enter only a Number")
# finally:
#       print("Execution COmpleted")


#Example:

# print("Welcome to SBI")
# print("Please Insert Card")
# balance=5000
# try:
#     check= input("Want to Check Balance? (y/n): ")
#     if check=="y":
#         print("Your bank balance is:", balance)

#     user=int(input("Enter the amount to withdraw: "))
#     if user<=0:
#         print("Please enter a valid amount to be withdrawn (greater than 0)")
#     elif user>balance:
#         print("Insufficient Balance")
#     else:
#         user_pin=int(input("Enter the PIN to withdraw: "))
#         print("Please collect the cash....")
#         total=balance-user
#         print("The Total Balance after withdrawing is: ",total)
# except ValueError:
#         print("Invalid input. Please enter valid a number")
# finally:
#     print("Thank You For Visiting.")

