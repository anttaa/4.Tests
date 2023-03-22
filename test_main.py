import pytest
import requests
from main import task_4_2, task_4_4, task_4_5, YaUploader


class TestCase:
    @pytest.mark.parametrize(
        'x', (
                ({'user1': [213, 213, 213, 15, 213],
                  'user2': [54, 54, 119, 119, 119],
                  'user3': [213, 98, 98, 35]}),
                ({'user1': [213, 213, 213, 15, 213],
                  'user3': [213, 98, 98, 35]}),
                ({'user3': [213, 98, 98, 35]})
        )
    )
    def test_task_4_2_count_values(self, x):
        result = task_4_2(x)
        assert len(result) == 6

    def test_task_4_4_result(self):
        result = task_4_4()
        assert result == 'y'

    def test_task_4_5_dict(self):
        result = task_4_5()
        expected_dict = {'2018-01-01': {'yandex': {'cpc': 100}}}
        assert result == expected_dict  # add assertion here

    @pytest.mark.parametrize(
        'x', (
                ('test'),
                ('test2'),
                ('test3'),
                ('test4')
        )
    )
    def test_create_dir(self, x):
        with open('token.txt') as f:
            token = f.read()
        assert token
        ya = YaUploader(token)
        result = ya.create_dir(x)
        assert result.status_code == 201  # Проверка на отработку запроса
        # Проверка на наличие папки в списке
        flag = False
        for item in ya.dirs()['_embedded']['items']:
            if x == item['name']:
                break
        assert flag == False
