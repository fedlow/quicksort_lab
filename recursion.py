def fibonacci(n, depth=0, trace=None):
    if trace is not None:
        trace.append("  " * depth + f"fib({n})")

    if n < 0:
        raise ValueError("n должно быть >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1, depth + 1, trace) + fibonacci(n - 2, depth + 1, trace)


def find_max(arr):
    if len(arr) == 0:
        raise ValueError("Пустой список")
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_max = find_max(arr[:mid])
    right_max = find_max(arr[mid:])
    return left_max if left_max >= right_max else right_max