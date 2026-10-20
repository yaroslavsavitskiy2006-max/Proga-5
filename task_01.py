# Задание 1. Пропускная способность записи (Т/с)

networks = {
    "Ethereum": 30,
    "Binance Smart Chain": 160,
    "Solana": 50000,
}


def tx_per_hour(net):
    """Сколько транзакций обработает каждая сеть за час."""
    return {name: tps * 3600 for name, tps in net.items()}


result = tx_per_hour(networks)

for name, cnt in result.items():
    print(f"{name}: {cnt:,} транзакций/час")

leader = max(result, key=result.get)
print(f"Лидер: {leader}")
