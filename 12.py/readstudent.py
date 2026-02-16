#read the student names from the students.txt file and display them
with open("Student/students.txt",'r') as file:
    names=file.readlines()
    print("Student names:")
    for name in names:
        print(name.strip())
if names:
    print("Total number of names stored:", len(names))
    longest_name=max(names, key=len).strip()
    print("Longest name:", longest_name,len(longest_name))