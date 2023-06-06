# def print_from(number: int) -> None:
#     print(number)
#     number -= 1
#     if number > 0:
#         print_from(number)

# print_from(4)

# def print_to(number: int) -> None:
#     if number > 0:
#         print_to(number - 1)
#         print(number)


# print_to(5)


# def double_fact(number: int) -> int:
#     if number == 1:
#         return 1
#     elif number == 2:
#         return 2
#     elif number > 2:
#         return number * double_fact(number - 2)

# assert double_fact(7) == 105
# assert double_fact(4) == 8
# assert double_fact(1) == 1
# assert double_fact(10) == 3840

# def tribonacci(number: int) -> int:
#     if number == 1 or number == 0:
#         return 0
#     elif number == 2:
#         return 1
#     elif number > 2:
#         return tribonacci(number - 1) + tribonacci(number -2) + tribonacci(number -3)

# assert tribonacci(0) == 0
# assert tribonacci(2) == 1
# assert tribonacci(4) == 2
# assert tribonacci(6) == 7
# assert tribonacci(7) == 13

# def get_combin(n: int, k: int) -> int:
#     if k == 0 or k == n:
#         return 1
#     if 0 < k < n:
#         return get_combin(n - 1, k) + get_combin(n - 1, k - 1)


# assert get_combin(5, 5) == 1
# assert get_combin(5, 2) == 10
# assert get_combin(3, 1) == 3
# assert get_combin(7, 0) == 1


def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
    
assert ackermann(3, 2) == 29
assert ackermann(3, 0) == 5
assert ackermann(1, 0) == 2
assert ackermann(3, 5) == 253
