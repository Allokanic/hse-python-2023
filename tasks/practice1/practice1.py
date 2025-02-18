def concatenate_strings(a: str, b: str) -> str:
    """
    Функция для сложения двух строк.
    Результат сложения запишите в переменную result.

    :param a: число
    :param b: число
    :return: результат сложения
    """

    # пиши свой код здесь
    result: str = a + b

    return result


def calculate_salary(total_compensation: int) -> float:
    """
    Функция расчета зарплаты, которую сотрудник получит после
    вычета налогов. Ставка налогообложения равна 13%.

    :param total_compensation: сумма зарплаты до вычета налога
    :return: сумма заплаты после вычета налога
    """

    # пиши свой код здесь
    total_compensation = float(total_compensation)

    result = total_compensation * 0.87

    return result
