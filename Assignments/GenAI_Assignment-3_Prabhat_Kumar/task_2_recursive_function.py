def factorial(n):
    if n<0:
        return f'{n} is not a positive number'
    if n==1 or n==0:
        return 1
    return  n * factorial(n-1)


print(factorial(5))
print(factorial(0))
print(factorial(-3))
    