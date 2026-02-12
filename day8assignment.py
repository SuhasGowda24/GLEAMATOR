#1.	Write a Python program that accepts a list of integers from the user and uses conditional statements and a for loop to separate the numbers into two different lists: one containing prime numbers and the other containing non-prime numbers. Store the results in a dictionary with keys "Prime" and "Non-Prime" and print the dictionary.

def prime_num(n):
	if n<=1:
		return False
	for i in range(2,n):
		if n%i==0:
			return False
	return True
numbers = list(map(int, input("Enter a list of numbers: ").split()))
prime = []
non_prime = []
for num in numbers:
    if prime_num(num):
        prime.append(num)
    else:
        non_prime.append(num)
        
result = {"Prime": prime, "Non-Prime": non_prime}
print(result)


#2.	Write a Python program that defines a function analyze_data(data) which takes a list of numbers as input and returns a dictionary containing the following:
# •	Total count of elements
# •	Sum of elements
# •	Maximum value
# •	Minimum value

def analyze_data(data):
    total_count = len(data) #Counts total number of elements in list
    total_sum = sum(data) #Calculates the sum of all numbers
    max_value = data[0] #assumes the first number is the maximum value, then compares it with each number in the list to find the actual maximum value
    min_value = data[0] #assumes the first number is the minimum value, then compares it with each number in the list to find the actual minimum value
    
    for num in data: #checks each number in list
        if num>max_value: #if number is greater than current max_value, then replace max_value with that number
            max_value = num
            if num<min_value: #if number is less than current min_value, then replace min_value with that number
                min_value = num
    return {
        "Total Count": total_count,
        "Sum": total_sum,
        "Max": max_value,
        "Min": min_value
    }

user=list(map(int, input("Enter 4 numbers: ").split()))
result = analyze_data(user)
print(result)


#3. Write a Python program using a while loop that keeps accepting numbers from the user until the user enters 0. Store only the unique numbers in a set. After termination, convert the set into a sorted tuple and display it.

unique_numbers = set() #creates an empty set to store unique numbers
while True: 
    num=int(input("Enter a number: ")) 
    if num<=0:
        break
    unique_numbers.add(num) #adds the number to the set, if it is not already present in the set
    print(unique_numbers) #prints the set of unique numbers after each input
sorted_tuple = tuple(sorted(unique_numbers)) #converts the set of unique numbers into a sorted tuple
print(sorted_tuple)

#4.	Write a Python program that takes a sentence as input and uses a dictionary to count the frequency of each character (excluding spaces). Display only those characters whose frequency is greater than 1.

sentence=input("Enter a sentence: ")
count_freq = {} #creates an empty dictionary to store character frequencies
for char in sentence: 
    if char!=" ": #checks if the character is not a space
        if char in count_freq: #if the character is already in the dictionary, increment its frequency
            count_freq[char] += 1
        else: 
            count_freq[char] = 1
for char, freq in count_freq.items(): #iterates through the dictionary items
    if freq > 1: #checks if the frequency of the character is greater than 1
        print(f"'{char}': {freq}") #prints the character and its frequency if it is greater than 1


#5.	Write a Python program that defines a function merge_lists(list1, list2) which:
# •	Accepts two lists
# •	Returns a tuple containing:
# 	A list of common elements
# 	A list of elements present in list1 but not in list2
# 	A list of elements present in list2 but not in list1
# Do not use set operations for comparison. Print the returned tuple.

def merge_lists(list1, list2):
    common_elements = [] #creates an empty list to store common elements
    list1=[]
    list2=[]
    
    for element in list1: #iterates through the first list
        if element in list2: #checks if the element is present in the second list
            if element not in common_elements:
                common_elements.append(element) #if it is present, adds it to the common_elements list
            else:
                list1.append(element) #if not present, adds it to the list1
    for element in list2: 
        if element not in list1: #checks if the element is not present in the first list
            list2.append(element) #if it is not present, adds it to the list2
    return (common_elements, list1, list2) #returns a tuple containing the common
            
list1=input("Enter the first list: ").split()
list2=input("Enter the second list: ").split()
result = merge_lists(list1, list2)
print(result) 
