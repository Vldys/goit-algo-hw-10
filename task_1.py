import timeit
coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}

    for coin in coins:
        count = amount // coin

        if count > 0:
            result[coin] = count
            amount = amount % coin

    return result


def find_min_coins(amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    last_coin = [0] * (amount + 1)

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                if dp[current_amount - coin] + 1 < dp[current_amount]:
                    dp[current_amount] = dp[current_amount - coin] + 1
                    last_coin[current_amount] = coin

    result = {}

    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


print("Жадный алгоритм:", find_coins_greedy(113))
print("Динамическое программирование:", find_min_coins(113))


amounts = [113, 1000, 10000]

for amount in amounts:
    greedy_time = timeit.timeit(
        lambda: find_coins_greedy(amount),
        number=10
    )

    dp_time = timeit.timeit(
        lambda: find_min_coins(amount),
        number=10
    )

    print(f"\nСумма: {amount}")
    print(f"Жадный алгоритм: {greedy_time:.6f} сек")
    print(f"Динамическое программирование: {dp_time:.6f} сек")
