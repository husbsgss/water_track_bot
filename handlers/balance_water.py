water_balance = 0

def balance_water(water: str) -> tuple[int, bool]:
    global water_balance
    water_balance += int(water)

    if water_balance >= 2000:
        water_balance = 0
        return 0, True   # (баланс, норма выполнена)

    return water_balance, False