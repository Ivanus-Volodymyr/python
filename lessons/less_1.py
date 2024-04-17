# # 1)
# st = 'as 23 fdfdg544'
# join = ','.join([char for char in st if char.isdigit()])
# print(join)
# 2)
# st = 'as 23 fdfdg544 34'
# res = ', '.join(''.join([char for char in part if char.isdigit()]) for part in st.split() if any(char.isdigit() for char in part))
# print(res)

# list comprehension
# 1)
# st = 'Hello world'
# res = list(''.join(st.upper()))
# print(res)
# 2)
# l = []
# num = 0
# while num < 50:
#     num += 1
#     if num % 2 == 1:
#         number = num ** 2
#         l.append(number)
# print(l)


# function
# 1)
# def list():
#     print([1, 2, 3, 4, 5, 6, 7, 8, 9])
# list()

# 2)
# def maxNum(a, b, c):
#     if a > b and a > c:
#         print(a)
#         return a
#     elif b > a and b > c:
#         print(b)
#         return b
#     elif c > a and c > b:
#         print(c)
#         return c
#
#
# l = maxNum(2, 6, 3)
# print(l)

# # 3)
# def num(*args):
#     m = min(args)
#     n = max(args)
#     print(n)
#     return m
#
#
# r = num(1, 2, 3, 4, 45)
# print(r)

# # 4)
# def max_value(li: list):
#     return max(li)
#
#
# print(max_value([1, 4, 5, 6, 6]))
#
#
# # 5)
# def min_value(li: list):
#     return min(li)
#
#
# print(min_value([1, 4, 5, 6, 6]))

# # 6)
# def sum_elements(numbers: list):
#     total = sum(numbers)
#     print(total)
#
#
# sum_elements([1, 4, 5, 6, 6])

# # 7)
# def avr(numbers: list):
#     total = sum(numbers)
#     count = len(numbers)
#     print(total / count)
#
#
# avr([1, 4, 5, 6, 6])


# my_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# # 1.
# print(min(my_list))
# # 2.
# s = set([x for x in my_list if my_list.count(x) == 1])
# print(list(s))
# # 3.
# new_list = ['X' if (i % 4 == 3) else my_list[i] for i in range(len(my_list))]
# print(new_list)

#
# def print_square(size):
#     if size < 2:
#         return 'Empty square'
#
#     print(size * '*')
#
#     for _ in range(size - 2):
#         print('*' + ' ' * (size - 2) + '*')
#
#     print(size * '*')
#
#
# print_square(8)


# def print_multiplication_table():
#     i = 1
#     while i <= 10:
#         j = 1
#         while j <= 10:
#             print(i * j, end='  ')
#             j += 1
#         print()
#         i += 1
#
#
# print_multiplication_table()


def main():
    my_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print('List:', my_list)
    print('1. Find the min number')
    print('2. Remove all duplicates')
    print('3. Replace every 4th value with X')
    print('4. Exit')

    value = input('Enter a number action: ')

    if value == '1':
        print(min(my_list))
    elif value == '2':
        s = set([x for x in my_list if my_list.count(x) == 1])
        print(list(s))
    elif value == '3':
        new_list = ['X' if (i % 4 == 3) else my_list[i] for i in range(len(my_list))]
        print(new_list)
    elif value == '4':
        return


main()
