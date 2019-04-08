def fib(n):
    if not isinstance(n, int):
        raise ValueError('n must be integer')
        
    if n == 0 or n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)
