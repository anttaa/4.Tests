import unittest
from main import task_4_2, task_4_4, task_4_5


class MyTestCase(unittest.TestCase):
    def test_task_4_2_count_values(self):
        result = task_4_2()
        self.assertEqual(len(result), 6)  # add assertion here

    def test_task_4_4_result(self):
        result = task_4_4()
        self.assertEqual(result, 'y')  # add assertion here

    def test_task_4_5_dict(self):
        result = task_4_5()
        expected_dict = {'2018-01-01': {'yandex': {'cpc': 100}}}
        self.assertDictEqual(result, expected_dict)  # add assertion here


if __name__ == '__main__':
    unittest.main()
