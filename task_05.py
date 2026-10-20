# Задание 5. Proof-of-Work (майнинг)

import hashlib


def mine(data, difficulty):
    """Подбор nonce, при котором хэш блока начинается с difficulty нулей."""
    prefix = "0" * difficulty
    nonce = 0
    while True:
        h = hashlib.sha256((data + str(nonce)).encode()).hexdigest()
        if h.startswith(prefix):
            return nonce, h
        nonce += 1


nonce, h = mine("block1", 4)
print(f"difficulty=4, nonce={nonce}")
print(f"hash={h}")
