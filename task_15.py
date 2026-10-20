# Задание 15. Дорожная карта кубитов: экстраполяция роста

generations = [127, 433, 1121]

# Коэффициенты роста между соседними поколениями = next / prev
growth_raw = [b / a for a, b in zip(generations, generations[1:])]
growth = [round(g, 2) for g in growth_raw]

# Средний темп — среднее арифметическое коэффициентов
avg = sum(growth_raw) / len(growth_raw)

# Прогноз = последнее значение × средний темп
forecast = round(generations[-1] * avg)

print(f"Поколения кубитов: {generations}")
print(f"Коэффициенты роста: {growth}")
print(f"Средний темп роста: x{avg:.2f}")
print(f"Прогноз следующего поколения: ~{forecast} кубитов")
