salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = spend - salary
current_spend = spend

# Расчет общей суммы расходов за 10 месяцев
for month in range(1, months):
    current_spend += current_spend * increase
    money_capital += (current_spend - salary)


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
