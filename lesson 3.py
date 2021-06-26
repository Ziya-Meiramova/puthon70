# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# else:
#     print("Stop")

# cnt = 0
# while True: # бесконечный цикл
#     cnt = cnt + 1
#     print(cnt)

# cnt = 10
# while cnt != 0:
#     print("Hi", cnt)
#     cnt = cnt - 2

# while True:
#     a = input()
#     if a == "Stop":
#         print('END')
#         break #выход с цикла
#     print(a)

#continue
#pass
# a = int(input())
# while a > 0:
#     a = a - 1
#     print(a)
#     if a == 5:
#         continue # игнорируй след код
#     if a == 2:
#         print("END")
#         break
#     print(a)

# вывести все четные числа до 10
# cnt = 11
# while cnt != 0:
#     cnt = cnt - 1
#     if cnt % 2 != 0:
#         continue
#     print(cnt)
#
# cnt = -1
# while cnt != 11:
#     cnt = cnt + 1
#     if cnt % 2 != 0:
#         continue
#     print(cnt)

# a = 100
# while True:
#     print('a')
#     n = input()
#     if n == 'S':
#         print("END")
#         break

# n = 9
# while n != 0:
#     pass # допиши сам
# print(n)

# задача 1
# вводим число, нужно вывести все
# квадраты до данного числа. ввод: 17 вывод: 1 4 9 16
# a = int(input())
# i = 1
# while i**2 <= a: # 5
#     print(i**2)
#     i = i + 1

# задача 2
# квадраты двойки ввод: 15 вывод: 1 2 4 8
# a = int(input())
# i = 1
# while i <= a: # 1, 2, 4, 8, 16,,
#     print(i)
#     i = i * 2

#задача 3 найти мин делитель числа
# a = int(input())
# i = 2
# while i <= a: # var 1
#     if a % i == 0:
#         print(i)
#         break
#     i = i + 1

# while a % i != 0: # var 2
#     i = i + 1
# print(i)

# является ли число точной степень. двойки
a = int(input()) # 8
i = 2
while i != a:
    if i > a: # i = 2 a = 11
        print("NO")
        break
    i = i * 2 # 11
else:
    print('YES')









