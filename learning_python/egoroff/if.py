"""if"""

numbers = list(map(int, input().split()))

for number in numbers:
    if number in [3, 5, 7, 9]:
        numbers.remove(number)

print(numbers)
