# Процентные ставки в банках
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit_sum = float(input("Введите сумму депозита: "))

# Список накопленных средств
deposit = [deposit_sum * (percentage_rate / 100) for percentage_rate in per_cent.values()]

# Переводим список float в int
deposit_int_list = [int(element) for element in deposit]

# Поиск максимального значения в списке deposit_int_list
max_deposit = max(deposit_int_list)

print(deposit_int_list)
print(f"Максимальная сумма, которую вы можете заработать — {max_deposit}")