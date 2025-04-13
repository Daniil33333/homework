def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.
    Видны первые 6 и последние 4 цифры, остальные заменены на **.
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Некорректный формат данных")
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция get_mask_account принимает на вход номер счета и возвращает его маску. Номер счета замаскирован
    и отображается в формате  **XXXX
    """
    if len(account_number) != 20 or not account_number.isdigit():
        raise ValueError("Некорректный формат данных")
    masked_account = f"**{account_number[-4:]}"

    return masked_account




