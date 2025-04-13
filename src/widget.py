import masks

def mask_account_card(str_1:str) -> str:
    if str_1[:4] == "Счет":
        return "Счет " + masks.get_mask_account(str_1[5:])
    else:
        return str_1[:-16] + masks.get_mask_card_number(str_1[-16:])

