from recursion import fibonacci, find_max
from sorts import quicksort


print("=== Фибоначчи: значения ===")
for n in range(0, 11):
    print(f"F({n}) = {fibonacci(n)}")

print("\n=== Стек вызовов для fib(5) ===")
trace = []
result = fibonacci(5, trace=trace)
for line in trace:
    print(line)
print(f"\nРезультат fib(5) = {result}")

print("\n=== Максимум списка (разделяй и властвуй) ===")
data = [3, 7, 1, 9, 4, 8, 2, 6, 5, 0]
print(f"Список: {data}")
print(f"Максимум: {find_max(data)}")

print("\n=== QuickSort ===")
unsorted = [10, 7, 8, 9, 1, 5, 3, 6, 2, 4]
print(f"До:  {unsorted}")
print(f"После: {quicksort(unsorted)}")