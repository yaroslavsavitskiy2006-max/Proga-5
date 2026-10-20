# Задание 3. Простейший блокчейн из блоков

import hashlib


class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        """SHA-256 от строки index + data + prev_hash."""
        s = f"{self.index}{self.data}{self.prev_hash}"
        return hashlib.sha256(s.encode()).hexdigest()


# Собираем цепочку из трёх блоков (у генезис-блока prev_hash = "0")
chain = []
prev = "0"
for i in range(3):
    block = Block(i, f"block{i}", prev)
    chain.append(block)
    prev = block.hash

for b in chain:
    print(f"Блок {b.index}: hash={b.hash[:16]}... prev={b.prev_hash[:16]}...")
