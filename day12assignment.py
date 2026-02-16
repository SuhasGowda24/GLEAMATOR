#Inheritance

#1. Create a base class called Employee.
# •	The class should contain attributes: name and salary.
# •	Create a method to display employee details.
# Now create a derived class called Manager that inherits from Employee.
# •	Add an additional attribute called department.
# •	Create a method to display manager details including department.
# •	Create an object of Manager and display all details.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def employee_details(self):
#         print("Employee Name:", self.name)
#         print("Employee Salary:", self.salary)
# class Manager(Employee):
#     def __init__(self,name, salary,department):
#         self.department=department
#         super().__init__(name, salary)
#     def manager_details(self):
#         super().employee_details()
#         print("Manager Department:", self.department)
        
# m=Manager("john",5000,"Marketing")
# m.manager_details()


#Polymorphism 

# 2. Create a class called Book.
# •	The class should have attributes: title and price.
# •	Use special method __add__() to add the prices of two books.
# •	Use special method __str__() to display book details properly.
# Create two book objects.
# •	Add both objects using + operator.
# •	Display total price.
# •	Print book details using print() function

# class Book:
#     def __init__(self,title,price):
#         self.title=title
#         self.price=price
#     def __add__(self,price):
#         self.price=self.price+price
#     def __str__(self,):
#         return f"{self.title}, {self.price}"
# b1=Book("Python Programming", 500)
# b2=Book("Full Stack", 700)
# print("Book 1:", b1)
# print("Book 2:", b2)
# total_price=b1.price+b2.price
# print("Total Price:", total_price)


# Encapsulation
# 3. Create a class called Student.
# •	Make the attributes name and marks private.
# •	Create setter methods to assign values.
# •	Do not allow marks to be less than 0 or greater than 100.
# •	Create getter methods to access the values.
# •	Create a method to calculate and display result:
# o	Marks ≥ 50 → Pass
# o	Marks < 50 → Fail
# Create an object and test all validations properly.

# class Student:
#     def __init__(self):
#         self.__name=''
#         self.__marks=0

#     def set_name(self, name):
#         self.__name = name
        
        
#     def set_marks(self, marks):
#         if marks>=0 and marks<=100:
#             self.__marks = marks
#         else:
#             print('invalid')
            
            
#     def get_name(self):
#         return self.__name
    
    
#     def get_marks(self):
#         return self.__marks
    
    
#     def result(self):
#         if self.__marks >= 50:
#             print("Pass")
#         else:
#             print("Fail")
            
# s1=Student()
# s1.set_name("Alice")
# s1.set_marks(-1)

# print(s1.get_name())
# print(s1.get_marks())
# s1.result()


# Built-in Modules:

# 4. Write a Python program that:
# •	Uses the math module to calculate square root and power of a number.
# •	Uses the random module to generate a random number between 1 and 100.
# •	Uses the datetime module to display the current date and time.
# Display all results clearly.


# import math
# import random
# import datetime

# def calc_sqrt(num):
#     return math.sqrt(num)
# def random_number():
#     return random.randint(1, 100)
# def date_time():
#     return datetime.datetime.now()
# print("Sqrt =",calc_sqrt(16))
# print("Random number=", random_number())
# print("Current date and time is=",date_time())


# Working with Text Files:
# 5. Write a Python program that:
# •	Accepts 5 student names from the user.
# •	Writes them into a text file named students.txt.
# •	Reads the contents of the file.
# •	Counts and displays the total number of names stored.
# •	Displays the longest name from the file.

