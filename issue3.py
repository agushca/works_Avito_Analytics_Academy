import unittest
from typing import List, Tuple

def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TestCase(unittest.TestCase):
    def test_data_2(self):
        data = ("A", "a", 1, (12,), "a")
        expected = [
            ("A", [0, 0, 0, 1]),
            ("a", [0, 0, 1, 0]),
            (1, [0, 1, 0, 0]),
            ((12,), [1, 0, 0, 0]),
            ("a", [0, 0, 1, 0]),
        ]
        output = fit_transform(data)
        self.assertIsInstance(output[0], tuple)
        self.assertIsInstance(output, list)
        self.assertEqual(expected, fit_transform(data))

    def test_fail_empty(self):
        with self.assertRaises(TypeError,):
            fit_transform()

    def test_fail_num(self):
        with self.assertRaises(TypeError):
            fit_transform(1)

    def test_fail_list(self):
        with self.assertRaises(TypeError):
            fit_transform("str", [1])