import masks

def mask_account_card(str_1:str) -> str:
    if str_1[:4] == "Счет":
        return "Счет " + masks.get_mask_account(str_1[5:])
    else:
        return str_1[:-16] + masks.get_mask_card_number(str_1[-16:])


def get_date (str_1:str) -> str:
    return str_1[8:10] + "." + str_1[5:7] + "." + str_1[:4]

print(get_date("2024-03-11T02:26:18.671407"))