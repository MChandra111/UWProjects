def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        print(b)
        a = b + a
        b = a + b

def lucas(n):
    a = 2
    b = 1
    for i in range(n):
        print(a)
        print(b)
        a = b + a
        b = a + b

def lucas_change(n, x, y):
    a = x
    b = y
    for i in range(n):
        print(a)
        print(b)
        a = b + a
        b = a + b

def sum_series(n, x=0, y=1):
    if (x == 0 & y == 1):
        fibonacci(n)
    else:
        lucas_change(n, x, y)

sum_series()
