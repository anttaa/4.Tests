
def task_4_2():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    ids_values = []
    for geo_ids in ids.values():
        ids_values += geo_ids
    return list(set(ids_values))


def task_4_4():
    stats = {'facebook': 55, 'y': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    return max(list(stats.items()), key=lambda i: i[1])[0]


def task_4_5():
    source = ['2018-01-01', 'yandex', 'cpc', 100]

    dct = source[-1]
    for n in source[-2::-1]:
        dct = {n: dct}
    return dct


if __name__ == '__main__':
    print(task_4_2())
    print(task_4_4())
    print(task_4_5())

