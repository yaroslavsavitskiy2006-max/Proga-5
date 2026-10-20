# Задание 8. Tangle (DAG): подтверждение двух транзакций

import random

random.seed(42)

N = 6
tangle = {}

for i in range(N):
    if i < 2:
        # Первые две транзакции — «вход» в граф, они ничего не подтверждают
        tangle[i] = []
    else:
        # Каждая новая транзакция подтверждает две случайные предыдущие
        tangle[i] = random.sample(range(i), 2)

for i in range(N):
    if tangle[i]:
        print(f"Транзакция {i} подтверждает: {tangle[i]}")
    else:
        print(f"Транзакция {i} подтверждает: — (начальная)")
