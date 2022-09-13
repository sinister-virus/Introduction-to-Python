def factorial(n):
    if n == 1:
        return 1

    elif n<1:
        if n%2==0:
            return factorial(-1*n)
        else:
            return -1*factorial(-1*n)

    else:
        x=n*factorial(n-1)
        return x


print(factorial(-2))
