#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    a, b = 0, 1
    for _ in range(length):
        fib.append(a)
        a, b = b, a + b
    print(fib)
