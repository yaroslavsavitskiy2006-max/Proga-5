# Задание 10. Индексатор: транзакции и баланс адреса

txs = [
    ("Alice", "Bob", 50),
    ("Bob", "Alice", 20),
    ("Alice", "Carol", 10),
]


def transactions_of(addr):
    """Все транзакции адреса (откуда, куда, сумма)."""
    return [t for t in txs if addr in (t[0], t[1])]


def balance(addr):
    """Баланс = сумма входящих − сумма исходящих."""
    incoming = sum(amount for frm, to, amount in txs if to == addr)
    outgoing = sum(amount for frm, to, amount in txs if frm == addr)
    return incoming - outgoing


addr = "Alice"
own = transactions_of(addr)

print(f"Транзакции {addr} ({len(own)}):")
for frm, to, amount in own:
    print(f"  {frm} -> {to}: {amount}")
print(f"Баланс {addr}: {balance(addr)}")
