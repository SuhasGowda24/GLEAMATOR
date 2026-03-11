try:
    num1=int(input("Enter the 1 num: "))
    num2=int(input("Enter the 2 num: "))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Enter the valid number")
    