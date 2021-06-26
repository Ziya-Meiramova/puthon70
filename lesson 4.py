# while x < y:
# i = счетчик, всегда с 0,  i = i + 1
# s = "Hello"

# for i in range(2, 11, 2):
#     print(i)

# вывод всех нечетный с помощью continue
#сontinue == игнорировать послед коды
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     if i == 7:
#         break
#     print(i)

# A - task
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         continue
#     print(i, end=" ")

#B
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# for i in range(a, b):
#     if i % d == c:
#         print(i)  # i = 1 if 1 % 2 == 1

# C
# a = int(input())
# b = int(input()) # 3 8
#
# for i in range(b + 1): # 3 8
#     if i**2 >= a and i**2 <= b:
#         print(i**2, end=" ")

#G
# n = int(input())
# cnt = 0
# for i in range(2, n+1):
#     if n % i == 0:
#         cnt+=1
# print(cnt)

# подсчет суммы всех элементов
# n = int(input()) # n = 6
# b = 0
# for i in range(n): # 6 4 29 5 3 1
#     a = int(input())
#
#     b = b + a
#     # b = 0 + 6
#     # b = 6 + 4
#     # b = 10 + 29
# print(b)


#кол четных и нечетных эл
# n = int(input())
# cnt_2 = 0
# cnt_3 = 0
# for i in range(n):
#     a = int(input())
#     if a % 2 == 0:
#         cnt_2 += 1
#     else:
#         cnt_3+=1
# print(cnt_2, cnt_3)

# max min
# n = int(input())
# mx = -4567890
# mn = 123456789
# for i in range(n):
#     a = int(input())
#     if a > mx:
#         mx = a
#     elif a < mn:
#         mn = a
# print(mx, mn)

# кол эл которые заканчиваютя на 7
# n = int(input())
# cnt_7 = 0
# for i in range(n): # 107 % 10 == 7 17 % 10 == 7
#     a = int(input())
#     if a % 10 == 7:
#         cnt_7+=1
#
# print(cnt_7)








