
def task_4_1():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

    geo_new = []
    for geo in geo_logs:
        for city, country in geo.values():
            if country.lower() == 'россия':
                geo_new.append(geo)

    for geo in geo_new:
        print(geo)


def task_4_2():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    # 1 вариант
    ids_values = []
    for geo_ids in ids.values():
        ids_values += geo_ids
    print(list(set(ids_values)))

    # 2 вариант
    ids_values = []
    for geo_ids in ids.values():
        for id in geo_ids:
            if id not in ids_values:
                ids_values.append(id)
    print(ids_values)


def task_4_3():
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]

    dct = {}
    for query in queries:
        key = len(query.split())
        if key not in dct:
            dct[key] = 1
        else:
            dct[key] += 1

    for key, value in sorted(dct.items()):
        print(f'Поисковых запросов из {key} слов(а) {round(value / len(queries) * 100)}%')


if __name__ == '__main__':
    print_hi('PyCharm')
