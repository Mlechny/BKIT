from operator import itemgetter
from math import inf

class Lib:
    """Библиотека"""
    def __init__(self, id, name, version, size, lang_id):
        self.id = id
        self.name = name
        self.version = version
        self.size = size
        self.lang_id = lang_id

class Lang:
    """Язык программирования"""
    def __init__(self, id, title):
        self.id = id
        self.title = title

class LibLang:
    """
    'Библиотеки языка программирования' для реализации связи многие-ко-многим
    """
    def __init__(self, lib_id, lang_id):
        self.lib_id = lib_id
        self.lang_id = lang_id

#Библиотеки
libs = [
    Lib(1, 'Algorithm', 1.24, 4348, 1),
    Lib(2, 'String', 1.15, 5258, 1),
    Lib(3, 'String', 1.15, 5258, 2),
    Lib(4, 'Mathpolib', 1.08, 9101, 2),
    Lib(5, 'Pony', 1.11, 4093, 3),
    Lib(6, 'Alamofire', 1.47, 7295, 4),
]

#Языки программирования
langs = [
    Lang(1, 'C++'),
    Lang(2, 'Python'),
    Lang(3, 'Ruby'),
    Lang(4, 'Swift'),
]

libs_langs = [
    LibLang(1, 1),
    LibLang(2, 1),
    LibLang(3, 2),
    LibLang(4, 2),
    LibLang(5, 3),
    LibLang(6, 4),
]

def main():
    """Основная функция"""
    #Соединение данных один-ко-многим
    one_to_many = [(li.name, li.version, li.size, la.title)
                   for la in langs
                   for li in libs
                   if li.lang_id == la.id]

    #Соединение данных многие-ко-многим
    many_to_many_temp = [(la.title, lila.lib_id, lila.lang_id)
                         for la in langs
                         for lila in libs_langs
                         if la.id == lila.lang_id]

    many_to_many = [(li.name, li.version, li.size, [la.title for la in langs if la.id == li_la.lang_id][0])
                    for li in libs
                    for li_la in libs_langs
                    if li.id == li_la.lib_id]
    '''
    Выведите спсиок языков программирования и связанных с ними библиотек из представленных,
    названия которых начинаются с буквы 'A'
    '''

    print('Задание В1')
    res_1 = list(filter(lambda i: i[0][0] == 'A', one_to_many))
    print(res_1)

    '''
    Выведите список названий языков программирования с минимальным размером библиотеки из представленных
    в каждом языке программирования, отсортированный по минимальному размеру библиотеки
    '''

    print('\nЗадание B2')
    min_sizes = {}
    for name, version, size, title in one_to_many:
        min_sizes[title] = min(min_sizes.get(title, inf), size)
    print(sorted(min_sizes.items(), key=itemgetter(1)))

    '''
    Выведите список связанных языков программирования и библиотек, отсортированный по номеру версии языка
    '''

    print('\nЗадание B3')
    res_3 = sorted(many_to_many, key=itemgetter(1))
    print(*res_3, sep = '\n')
    print('\nСпасибо за тестирование!')

if __name__ == '__main__':
    main()