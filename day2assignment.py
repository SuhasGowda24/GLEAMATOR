name = input("Enter your name: ")
marital_status = input("single/married: ")
age = int(input("Enter your age:"))
employment_status = input("emp/unemp?: ")
gender = input("Male/Female?: ")
location = input("Address Please: ")
print(f"Ah, {name}, the {marital_status} legend of {location}! At {age} years young, you're {employment_status} and rocking that {gender} vibe. If life were a sitcom, you'd be the star – dodging plot twists and stealing the show!")
# print(f"Hello {name}, you are {age} years old, {marital_status}, {employment_status}, {gender}, living in {location}.")
# if marital_status == "single" and (employment_status == "unemp" or employment_status == "unemployed"):
#     print(f"Sorry {name}, being single and unemployed at {age} is tough, but keep pushing!")
# else:
#     print(f"Hello {name}, you are {age} years old, {marital_status}, {employment_status}, {gender}, living in {location}.")






#1
# num = input("Enter the number:")
# if num.isdigit():
#     print("The number is Int")
# if num.isalpha():
#     print("The Number is a String")
# if '.' in num and num.replace('.', '',).isdigit():
#     print("The number is Float")

    
# try:
#     num = int(num)
#     print("The number is integer")
# except ValueError:
#     try:
#         num = float(num)
#         print("The number is Float/Decimal")
#     except ValueError:
#         print("It is not a number")
