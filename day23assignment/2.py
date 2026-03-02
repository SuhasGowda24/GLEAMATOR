#11. Write a program to read and print a 1D array
# N = int(input("Enter the arrays: "))
# arr = []
# for i in range(N):
#     arr.append(int(input()))
# print(*arr)


#12. Write a program to read and print a 2D array (matrix)
# data=list(map(int, input().split()))
# R=data[0]
# C=data[1]
# matrix=[]
# index=2
# for i in range(R):
#     row = []
#     for j in range(C):
#         row.append(data[index])
#         index += 1
#     matrix.append(row)
# for row in matrix:
#     print(*row)
        
        
#13. Write a program to find the size of a 1D array
# N = int(input("Enter the number of element: "))
# arr = list(map(int, input("Enter the array: ").split()))
# print(len(arr))


#14. Write a program to traverse an array using a loop.
# N=int(input("Enter the size of the array: "))
# arr=list(map(int, input().split()))
# for i in range(N):
#     print(arr[i], end=" ")
    
#15. Write a program to traverse an array in reverse order.
# N=int(input(("Enter the array: ")))
# arr=list(map(int, input("Enter the list of elements").split()))
# for i in range(N-1,-1,-1):
#     print(arr[i],end="")
    
#16. Write a program to traverse a 2D array.
R = int(input())
C = int(input())
matrix = []
for i in range(R):
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()    