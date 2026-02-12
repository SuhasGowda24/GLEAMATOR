#1. Create a class called Circle. Add an attribute radius. After creating the object, assign the radius value. Create a method to calculate and print the area of the circle. Display the result in a proper sentence.
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
        
#     def calculate_area(self):
#         area = 3.14*(self.radius**2)
#         print(f"The area of the circle with radius {self.radius} is: {area}")
# circle = Circle(2)
# circle.calculate_area()


# Create a class called ExamResult. Add attributes student_name and marks. After creating the object, assign the values. Create a method that checks whether the student passed or failed:
# •	Pass if marks are greater than or equal to 40
# •	Fail if marks are less than 40
# Print a detailed result message.

# class ExamResult:
#     def __init__(self,student_name,marks):
#         self.student_name=student_name
#         self.marks=marks
        
#     def check_result(self):
#         if self.marks>=40:
#             print(f"{self.student_name} has passed with marks: {self.marks}")
#         else:
#             print(f"{self.student_name} has failed with marks: {self.marks}")
# student1=ExamResult("Suhas",50)
# student1.check_result()


# 3. Create a class called Rectangle. Use a constructor to initialize length and breadth. Create methods to calculate and print:
# •	Area
# •	Perimeter
# Display both results clearly.

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def calculate_area(self):
#         area=self.length*self.breadth
#         print(f"The area with length {self.length} and breadth {self.breadth} is: {area}")
#     def calculate_perimeter(self):
#         perimeter=2*(self.length+self.breadth)
#         print(f"The perimeter with length {self.length} and breadth {self.breadth} is: {perimeter}")
# rectangle=Rectangle(2,5)
# rectangle.calculate_area()
# rectangle.calculate_perimeter()


# 4. Create a class called Product. Use a constructor to initialize product_name and price. Create two objects with different values. Write a method to compare the prices and print which product is more expensive.

# class Product:
#     def __init__(self, product_name,price):
#         self.product_name=product_name
#         self.price=price
#     def compare_prices(self, other):
#         if self.price > other.price:
#             print(f"{self.product_name} is more expensive than {other.product_name}")
#         else:
#             print(f"{other.product_name} is more expensive than {self.product_name}")
# product1=Product("Laptop",70000)
# product2=Product("Smartphone",50000)
# Product.compare_prices(product1,product2)


#5. Create a class called BankAccount. Use a constructor to initialize account_holder and balance. Create methods to:
# •	Deposit money
# •	Withdraw money
# •	Display final balance

class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,money):
        self.balance+=money
        print(f"{money} deposited. New balance is: {self.balance}")
    def withdraw(self,money):
        self.balance-=money
        print(f"{money} withdrawn. New balance after withdrawal is: {self.balance}")
user1=BankAccount("Suhas",10000)
user1.deposit(5000)
user2=BankAccount("pannaga",10000)
user2.withdraw(100)
user1.withdraw(999)
