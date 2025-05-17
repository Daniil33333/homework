import masks


def mask_account_card(str_1: str) -> str:
    """
    Возвращает строку с замаскированным номером
    """
    if str_1[:4] == "Счет":
        return "Счет " + masks.get_mask_account(str_1[5:])
    else:
        return str_1[:-16] + masks.get_mask_card_number(str_1[-16:])


def get_date(str_1: str) -> str:
    """
    Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    return str_1[8:10] + "." + str_1[5:7] + "." + str_1[:4]
