# Задание 11. Статистика запросов по сабграфам

log = [
    ("uniswap", 5000),
    ("aave", 3500),
    ("uniswap", 4000),
    ("compound", 2000),
    ("aave", 5000),
    ("uniswap", 3500),
    ("compound", 2500),
]

# Суммируем количество запросов по ключу-сабграфу
d = {}
for sg, cnt in log:
    d[sg] = d.get(sg, 0) + cnt

for sg, cnt in d.items():
    print(f"{sg}: {cnt:,} запросов")

print(f"Самый нагруженный: {max(d, key=d.get)}")
print(f"Всего запросов: {sum(d.values()):,}")
