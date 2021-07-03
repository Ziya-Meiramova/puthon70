# a = [1, 2, "Hello", True, 6.7]
# # print(len(a))
# for i in range(len(a)): # 0 1 2 3 4
#     print(a[i])
#     print(a[4])
#     break
# for i in a: # i = a 1) i = 1 2) i = 2 3) i = "Hello
#     print(i, end=" " )

# task 1
#вывести все нечетные числа из списка
# n = int(input())
# b = []
# for i in range(n):
#     a = int(input()) # 4 7 3 2
#     if a % 2 == 0:
#         b.append(a) # 4 2  # append = добавление с конца
# for i in b: # b = [4, 2] 1) i = 4 2) i = 2
#     print(i, end=" ")


# task 2 подсчитать сколько положительный
# и отрицательных элементов в списке
# 1. ввести n, for + a, заполняете в лист пустой
# n = int(input())
# b = []
# cnt_more = 0
# cnt_less = 0
# for i in range(n):
#     a = int(input())
#     b.append(a) # b = [-6, 0,55, 23, -78]
# for i in b:
#     if i > 0:
#         cnt_more+=1
#     elif i < 0:
#         cnt_less+=1
#     else:
#         continue
# print(cnt_more, cnt_less)

# 4 5 2 5 6 -8 -23456 0
# a = []
# while True:
#     t = int(input()) # 3 -8 7 4 0
#     if t != 0:
#         a.append(t)
#     else:
#         a.sort() # сортирует список
#         for i in a:
#             print(i, end=" ")

# task D from informatics
# вывести все числа которые больше пред

# n = int(input())
# a = []
# for i in range(n):
#     t = int(input())
#     a.append(t)
# for i in range(1, len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end=" ")

# n = input() # n = "1 2 3 4 5"
# arr = n.split() # arr = ['1', '2', '3', '4', '5']
# arr2 = [] # arr2 = [1,2, 3, 4, 5]
# for i in arr:
#     arr2.append(int(i))
# for i in range(1, len(arr2)):
#     if arr2[i] > arr2[i-1]:
#         print(arr2[i], end=" ")


# f = 7.9 # float -> int
# print(int(f))

# list in list
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in a: #1) i = [1, 2, 3] 2) i = [4, 5, 6]
#     for j in i: #1) j = 1 2) j = 2 3) j = 3
#         print(j, end=" ")
#     print()
# print(a[0][1])
# print(a[1][0])
# a.append(["hi", "students"])
# print(a)

# task E
# n = input()
# a = n.split()
# arr2 = []
# for i in a:
#     arr2.append(int(i))
# for i in range(len(arr2)):
#     if arr2[i] > 0 and arr2[i-1] > 0 or arr2[i] < 0 and arr2[i-1] < 0:
#         print(arr2[i-1], arr2[i])
#         break

# max
n = input()
arr = n.split()
arr2 = []
for i in arr:
    arr2.append(int(i))

mx = -1234567890
index = 0

for i in range(len(arr2)): # arr2 = [4,-7, 8, 2, 23456, 5]
    if arr2[i] > mx:
        mx = arr2[i] # 4 8 23456
        index = i # 0 2 4
print(mx, index)

