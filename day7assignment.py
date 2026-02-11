#1. Write a Python program to create a function named find_largest(a, b, c) that accepts three numbers as arguments and returns the largest number among them. Call the function and display the result.

# def find_largest(a,b,c):
#     a=int(input("Enter a: "))
#     b=int(input("Enter b: "))
#     c=int(input("Enter c: "))
#     if a>b and a>c:
#         print("a is the largest")
#     elif b>a and b>c:
#         print("b is the largest")
#     elif c>a and c>b:
#         print("c is the largest")
#     elif a==b and a==c:
#         print("The largest is", a,b,c )
#     else:
#         print("c is the largest")
#     find_largest(a,b,c)

def find_largest(a,b,c):
    return max(a,b,c)
a=int(x=input(prompt="Enter a: "))
b=int(x=input(prompt="Enter b: "))
c=int(x=input(prompt="Enter c: "))
largest=find_largest(a=a,b=b,c=c)
print("the largest number is: ",largest)


#2.Write a Python program to create a function named find_largest(a, b, c) that accepts three numbers as arguments and returns the largest number among them. Call the function and display the result.

def sum_of_list(numbers):
    return sum(numbers)
numbers = [1, 2, 3, 4, 5]
result = sum_of_list(numbers=numbers)
print(f"The sum of {numbers} is: {result}")

    
#3. Write a Python program to perform the following operations:
# •	Create a list of 5 integers.
# •	Add one new element to the list.
# •	Convert the list into a tuple.
# •	Display both the list and the tuple.

list=[1,2,3,4,5]
list.append(6)
print(list)

list_tuple=tuple(list) #converts lists into tuple
print("lists are:",list)
print("tuples are:",list_tuple)


#4. Write a Python program to create two sets with some common elements. Perform and display the following operations:
# •	Union
# •	Intersection
# •	Difference

set1={1,2,3,4,5}
set2={1,2,3,4,5}
print(set1)
print(set2)
union=set1.union(set2) #union-all unique elements from both sets
print("Union:",union)
intersection=set1.intersection(set2) #Intersection-common elements in both sets
print("Intersection:",intersection)
difference=set1.difference(set2)
print("Difference(set1-set2):",difference)
#       OR
set1={1,2,3,4,5}
set2={6,5,4,8,1}
print(set1)
print(set2)
union=set1.union(set2) #union-combines all unique elements from both sets into one single set(removes duplicate)
print("Union:",union)
intersection=set1.intersection(set2) #Intersection-common elements in both sets
print("Intersection:",intersection)
difference=set1.difference(set2) #finds elements present in set1 but not in set2
print("Difference(set1-set2):",difference)


#5. Write a Python program to create a dictionary with student names as keys and their marks as values. Perform the following operations:
# •	Add a new student
# •	Update the marks of an existing student
# •	Display all students and their marks

dictionary={"Suhas":90, "Praveen":91, "Pannaga":92}
print(dictionary)

dictionary["Ritesh"]=93
print(dictionary)

dictionary["Suhas"]=99
print(dictionary["Suhas"])

print("All the students marks:")
for name, marks in dictionary.items(): #dictionary.items() returns both student name and marks.name stores the key (student name).marks stores the value (student marks).
    print(name,":",marks)


#6.  Write a Python program to create a dictionary representing items and their prices. Create a function calculate_total(cart) that calculates and returns the total amount of all items. Display the final bill amount.

items={"Pen": 10,"Notebook": 50,"Pencil": 5,"Eraser": 3}
def calculate_total(cart): #defining function
    total=0 #initial value
    for price in cart.values(): #cart.values gives only the prices form dictionary
        total+=price #adds each files to total amount
    return total
total_amount=calculate_total(items)
for items, price in items.items():
    print(items,":",price)
# print(items)
print("The total amount is:",total_amount)
