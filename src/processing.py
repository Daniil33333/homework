def filter_by_state(dict_list: list[dict], state:str = 'EXECUTED') -> list[dict]:
    """
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state
    соответствует указанному значению.
    """
    result_list = []
    for el in dict_list:
        if el['state'] == state:
            result_list.append(el)

    return result_list


def sort_by_date(date_list: list[dict], order=True) -> list[dict]:
    """
    Функция возвращает новый список, отсортированный по дате (date).
    """
    result_list = sorted(date_list, key=lambda x: x['date'], reverse=order)
    return result_list

