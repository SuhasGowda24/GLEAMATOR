#Amstrong

# a=153
# a=int(input("Enter a number: "))
# a=153
# sum=0
# temp=a
# while temp>0:
#     result=temp%10
#     sum+=result ** 3
#     temp//=10
# if sum==a:
#     print("Amstrong")
# else:
#     print("Not Amstrong")
    
# a=153
# original=a
# sum=0
# # temp=a
# while original>0:
#     digit=original%10
#     sum+=digit**3
#     digit//=10
# if sum==a:
#     print("Amstrong")
# else:
#     print("Not Amstrong")


# a=int(input("Enter a number: "))
# sum=0
# temp=a
# count=0
# if temp==0:
#     count=1
# else:
#     while temp>0:
#         count+=1
#         temp//=10
# if temp==0:
#     while temp>0:
#         digit=temp%10
#         sum+=digit ** 3
#         temp//=10
# if sum==a:
#     print("Amstrong")
# else:
    # print("Not Amstrong")
    
    
# List count how many are positive, negative and zero
# a=[1,-2,3,0,-4,0,5,0.1,-0.5]
# positive=0
# negative=0
# zero=0
# for i in a:
#     if i>0:
#         positive+=1
#     elif i<0:
#         negative+=1
#     else:
#         zero+=1
# print("Number of Positive:",positive)
# print("Number of Negative:",negative)
# print("Number of Zeros:",zero)


# Find the largest number in a list
# a=[1,-2,3,0,-4,0,5,0.1,-0.5]
# largest=a[0]
# # smallest=0
# for i in a:
#     if i>largest:
#         largest=i
# print("The Maximum number is:", largest)
# for i in a:
#     if i<largest:
#         largest=i
# print("The Minimum number is:", largest)


# Concatination of 2 lists
# a=[1,2,3]
# b=[4,5,6]
# c=a.extend(b)
# print(a)


#Difference of for loop and while loop practically
# for i in range(1,5):
#     print(i)
# print("-------")
# j=1
# while j<5:
#     print(j)
#     j+=1


#To find the round of a number
# num=10.5
# print(num/5)