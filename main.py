import requests


def task_4_2(ids: list):
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


class YaUploader:
    def __init__(self, token: str):
        self.url_upload = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.token = token

    def get_header(self):
        return {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def create_dir(self, name):
        return requests.put(f'{self.url_upload}?path={name}', headers=self.get_header())

    def dirs(self):
        return requests.get(f'{self.url_upload}?path=/', headers=self.get_header()).json()
