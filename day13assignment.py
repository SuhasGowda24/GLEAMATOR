# 1. You are given a CSV file named students.csv containing:
# id,name,marks
# 1,Anu,85
# 2,Ravi,45
# 3,Meena,72
# 4,Kiran,30

# Perform the following:
# 1.	Read the CSV file.
# 2.	Display only students who scored more than 50.
# 3.	Count how many students failed (marks < 50).

import csv
with open('students.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['id','Name','marks'])
    writer.writerow([1,'Anu',85])
    writer.writerow([2,'Ravi',45])
    writer.writerow([3,'Meena',72])
    writer.writerow([4,'Kiran',30])
print('csv file created')

with open('students.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

    file.seek(0)
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        id,name,marks=row
        if int(marks)>=50:
            print("Students passed are:",name)
            
    count=0
    file.seek(0)
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        id,name,marks=row
        if int(marks)<50:
            count+=1
            print("Students failed are:",name)

