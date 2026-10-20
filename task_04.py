# Задание 4. Хеширование SHA-256

import hashlib


def sha256_str(s):
    """SHA-256-хэш произвольной строки."""
    return hashlib.sha256(s.encode()).hexdigest()


h = sha256_str("blockchain")
print(f"SHA-256('blockchain') =\n{h}")
