# Задание 14. Алгоритм Шора: факторизация числа


def factorize(n):
    """Классическая факторизация — разложение числа на простые множители."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:  # остаток — тоже простой множитель
        factors.append(n)
    return factors


for num in (15, 21, 91):
    print(f"{num} = {' x '.join(map(str, factorize(num)))}")
