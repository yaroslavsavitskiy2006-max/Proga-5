# Задание 12. Цифровая подпись (упрощённая модель)

import hashlib

PRIVATE_KEY = "my-private-key-2026"


def sign(message, private_key):
    """Подпись = SHA-256 от (сообщение + приватный ключ)."""
    return hashlib.sha256((message + private_key).encode()).hexdigest()


def verify(message, signature, private_key):
    """Проверка: пересчитываем подпись и сравниваем с переданной."""
    return sign(message, private_key) == signature


msg = "Alice sends 10 BTC to Bob"
signature = sign(msg, PRIVATE_KEY)

print(f"Подпись: {signature[:25]} ...")
print(f"Проверка верной подписи: {verify(msg, signature, PRIVATE_KEY)}")

tampered = "Alice sends 100 BTC to Bob"
print(f"Проверка при подмене сообщения: {verify(tampered, signature, PRIVATE_KEY)}")
