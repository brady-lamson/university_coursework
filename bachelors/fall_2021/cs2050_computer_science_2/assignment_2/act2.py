def func(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * func(a, b-1)

print(func(6,3))