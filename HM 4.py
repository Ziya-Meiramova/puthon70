# #task 1
# n = int(input()) # 4 1: i = 0 2: i = 1 3: i =2 4: i = 3
# cnt = 0
# for i in range(n):
#     a = int(input()) # 3 6 4 0
#     if a == 0:
#         cnt = 1
# if cnt == 1:
#     print("YES")
# else:
#     print('NO')
#

# task 2
# n = int(input())
# cnt_0 = 0
# cnt_more = 0
# cnt_less = 0
# for i in range(n): # 3 4 -8 0
#     a = int(input())
#     if a == 0:
#         cnt_0 += 1
#     elif a > 0:
#         cnt_more += 1
#     else:
#         cnt_less += 1
# print(cnt_0, cnt_more, cnt_less)

# task 3
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# for x in range(1000):
#     if (a * x**3 + b * x**2 + c * x + d) == 0:
#         print(x, end=" ")

#task 4
# n = int(input())
# cnt = 0
# for i in range(n):
#     a = int(input())
#     if a == 0:
#         cnt = cnt + 1
# print(cnt)

#task 5
# n = int(input())
# cnt_1 = 0
# cnt_2 = 0
# for i in range(n):
#     a = int(input())
#     if a % 10 == 1:
#         cnt_1 += 1
#     elif a % 10 == 2:
#         cnt_2 += 1
# print(cnt_2, cnt_1)





