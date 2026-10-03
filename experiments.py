import random
import time
import matplotlib.pyplot as plt

from sorts import quicksort, insertion_sort


def measure(func, arr, repeats=3):
    total = 0.0
    for _ in range(repeats):
        data = arr.copy()
        start = time.perf_counter()
        func(data)
        total += time.perf_counter() - start
    return total / repeats


def main():
    random.seed(42)

    sizes = [10, 100, 1000, 2000, 5000, 10000, 20000]
    qs_times = []
    ins_times = []

    for n in sizes:
        arr = [random.randint(1, 100_000) for _ in range(n)]

        qs = measure(quicksort, arr, repeats=5 if n <= 2000 else 3)
        ins = measure(insertion_sort, arr, repeats=5 if n <= 2000 else 3)

        qs_times.append(qs)
        ins_times.append(ins)

        print(f"n={n:6d} | quicksort={qs:.6f} c | insertion={ins:.6f} c")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, qs_times, marker="o", label="QuickSort")
    plt.plot(sizes, ins_times, marker="s", label="Сортировка вставками")
    plt.xlabel("Размер списка n")
    plt.ylabel("Среднее время, сек")
    plt.title("QuickSort vs сортировка вставками")
    plt.legend()
    plt.grid(True)
    plt.savefig("quicksort_comparison.png", dpi=150)
    plt.show()

    # Сохранение таблицы в Markdown
    lines = ["| n | QuickSort, с | Вставками, с |",
             "|---|---|---|"]
    for n, qs, ins in zip(sizes, qs_times, ins_times):
        lines.append(f"| {n} | {qs:.6f} | {ins:.6f} |")

    with open("results.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("\nТаблица сохранена в results.md")


if __name__ == "__main__":
    main()