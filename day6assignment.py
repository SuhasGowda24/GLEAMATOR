print("Welcome to SBI")
print("Please Insert Card")
balance=5000
try:
    check= input("Want to Check Balance? (y/n): ")
    if check=="y":
        print("Your bank balance is:", balance)

    user=int(input("Enter the amount to withdraw: "))
    if user<=0:
        print("Please enter a valid amount to be withdrawn (greater than 0)")
    elif user>balance:
        print("Insufficient Balance")
    else:
        user_pin=int(input("Enter the PIN to withdraw: "))
        print("Please collect the cash....")
        total=balance-user
        print("The Total Balance after withdrawing is: ",total)
except ValueError:
        print("Invalid input. Please enter valid a number")
finally:
    print("Thank You For Visiting.")





    

