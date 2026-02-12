#Classes and Objects
# class College:
#     def college_name(self, name):
#         print("college name is:",name)
#     def student(self, name):
#         print("student name is:",name)
#     def course(self, name):
#         print("course name is:",name)
#     def passout_year(self, name):
#         print("passout year is:",name)

# college_name=College()        
# student=College()
# course=College()
# passout_year=College()

# college_name.college_name("kssem")
# student.student("suhas")
# course.course("BE")
# passout_year.passout_year("2026")



# class Office:
#     def company_name(self, name):
#         print("Company name:",name)
#     def employee(self, name):
#         print("Employee name:",name)
#     def position(self, name):
#         print("Position placed is for:",name)
#     def salary(self, name):
#         print("Estimated Salary is:",name)
#     def work_hours(self, name):
#         print("work hours is:",name)

# Office().company_name("Gleamator")
# Office().employee("Suhas")
# Office().position("Software Developer")
# Office().salary("360000")
# Office().work_hours("10am-4pm")


# class Phone:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         self.model = "Galaxy S21"

# phone1 = Phone("Samsung", "black")
# print(phone1.brand, phone1.color, phone1.model)


# class Earpods:
#     def __init__(self,brand,color,price,battery_usage,user_experience):
#         self.brand=brand
#         self.color=color
#         self.price=price
#         self.battery_usage=battery_usage
#         self.user_experience=user_experience
# earpod=Earpods("Boult","White","1k","4 hrs","Good sound quality, Includes noise cancellation")
# print(earpod.brand)
# print(earpod.color)
# print(earpod.price)
# print(earpod.battery_usage)
# print(earpod.user_experience)


class about_me:
    def __init__(self,name,age,college,usn,aim):
        self.name=name
        self.age=age
        self.college=college
        self.usn=usn
        self.aim=aim
Myself=about_me("Suhas",21,"KSSEM","CS113","To become a successful AI Engineer")
print("Name:",Myself.name)
print("Age:",Myself.age) 
print("College:",Myself.college)
print("USN:",Myself.usn) 
print("My Aim is",Myself.aim)