"""Sample Input:

99
Sample Output:

Для числа 99 предыдущим будет число 98.
Для числа 99 следующим будет число 100.
"""

number = int(input())
print(f"Для числа {number} предыдущим будет число {number - 1}.",
      f"Для числа {number} следующим будет число {number + 1}.",
      sep="\n")