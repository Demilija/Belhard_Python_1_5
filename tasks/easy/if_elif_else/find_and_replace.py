"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Пользователь вводит 2 строки. Если вторая строка есть первой, то нужно
в первой строке поменять регистр на обратный, а во второй сделать первую букву
большой, а остальные маленькими
ПРИМЕРЫ
--------------------------------------------------------------------------------
- ('Как твои дела', 'Как') -> ('кАК ТВОИ ДЕЛА', 'Как')
- ('добРый день коЛЛеги', 'день') -> ('ДОБрЫЙ ДЕНЬ КОллЕГИ', 'День')
- ('добРый день коЛЛеги', 'тень') -> ('добРый день коЛЛеги', 'тень')
"""


def find_and_replace(check_str: str, search_str: str) -> tuple:
    """Если вторая строка есть в первой, то в первой меняет регистр, а вторую
    делает с большой буквы
    :param check_str: строка для проверки
    :type check_str: str
    :param search_str: строка, которую будем искать
    :type search_str: str
    :return: обработанные строки
    :rtype: tuple
    """

    if search_str in check_str:
        check_str = check_str.swapcase()
        search_str = search_str.capitalize()

    return check_str, search_str


if __name__ == '__main__':
    c_str = input('Введите строку для проверки: ')
    s_str = input('Введите строку, которую будем искать: ')
    print(f'Результат: {find_and_replace(c_str, s_str)}')
