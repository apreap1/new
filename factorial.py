def factorial_with_cache():
    cache = {}

    def calc(n):
        if n < 0:
            raise ValueError("Number can't be negative")
        result = 1
        for val in range(1, n + 1):
            if val in cache:  # перевіряємо чи результат вєе є у кеші?
                result = cache[val]  # то беремо результат з кеша (з словника)
                print(f"{val} in cache {result}")
            else:
                result = val * cache.get(val - 1, 1)  # щоб не було помилки
                cache[val] = result  # присвоюю результат
                print(f"{val} not in cache {result}")
        return result
    return calc


factorial = factorial_with_cache()
f3 = factorial(3)
print(f"f(3): {f3}")

f5 = factorial(5)
print(f"f(5): {f5}")


f4 = factorial(4)
print(f"f(4): {f4}")
