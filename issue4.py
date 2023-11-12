from typing import List, Tuple
import pytest


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


def test1_empty_input():
    with pytest.raises(TypeError):
        fit_transform()


def test1_invalid_input():
    with pytest.raises(TypeError):
        fit_transform(0)


def test2():
    result = fit_transform('a', 'b', 'c')
    expected = [
        ('a', [0, 0, 1]),
        ('b', [0, 1, 0]),
        ('c', [1, 0, 0])
    ]
    assert result == expected


def test4():
    assert fit_transform(['Msk', 'Ny', 'Msk', 'Spb']) == [
        ('Msk', [0, 0, 1]),
        ('Ny', [0, 1, 0]),
        ('Msk', [0, 0, 1]),
        ('Spb', [1, 0, 0])
    ]