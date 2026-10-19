water_balances = {}

def balance_water(user_id, water):
    current = water_balances.get(user_id, 0)   # если нет — 0
    current += int(water)
    if current >= 2000:
        water_balances[user_id] = 0
        return 0, True
    water_balances[user_id] = current
    return current, False