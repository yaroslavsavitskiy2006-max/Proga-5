# Задание 6. Корень дерева Меркла

import hashlib


def merkle_root(transactions):
    """Корень дерева Меркла: хэши попарно, пока не останется один корень."""
    # Листья — хэши каждой транзакции
    level = [hashlib.sha256(tx.encode()).hexdigest() for tx in transactions]

    while len(level) > 1:
        # Если на уровне нечётное число элементов — дублируем последний
        if len(level) % 2 == 1:
            level.append(level[-1])
        # Хэшируем пары соседних элементов
        level = [
            hashlib.sha256((level[i] + level[i + 1]).encode()).hexdigest()
            for i in range(0, len(level), 2)
        ]

    return level[0]


txs = ["tx1", "tx2", "tx3", "tx4"]
print(f"Merkle root: {merkle_root(txs)}")
