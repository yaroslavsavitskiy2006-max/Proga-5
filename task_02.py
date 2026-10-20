# Задание 2. Соотношение операций чтения к записи


def read_ops_range(write_ops):
    """Минимальное и максимальное число операций чтения в секунду."""
    return write_ops * 100, write_ops * 10_000


writes = 500
mn, mx = read_ops_range(writes)

print(f"Записей в секунду: {writes}")
print(f"Минимум чтений/с: {mn:,}")
print(f"Максимум чтений/с: {mx:,}")
