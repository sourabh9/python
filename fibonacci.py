#!/usr/bin/python
c = []


def get_numbers(help_text):
    return int(input(help_text))


def fibonacci(n1):
    for i in range(0, n1):
        if (i == 0) | (i == 1):
            c.append(i + 1)
        else:
            c.append((c[i - 2]) + (c[i - 1]))
    return c


a = get_numbers("How many Fibonacci number you want to generate:")
print(fibonacci(a))
