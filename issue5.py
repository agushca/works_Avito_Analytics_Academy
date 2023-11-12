import pytest
from unittest.mock import patch
import current_year


@patch('current_year.json.load')
def test_year_extraction(mock_json_load):
    mock_json_load.return_value = {'currentDateTime': '2023-11-05T16:30Z'}
    result = current_year.what_is_year_now()
    assert result == 2023


@patch('current_year.json.load')
def test_year_format(mock_json_load):
    mock_json_load.return_value = {'currentDateTime': 'invalid_format'}
    with pytest.raises(ValueError):
        current_year.what_is_year_now()


@patch('current_year.json.load')
def test_year_ymd_format(mock_json_load):
    mock_json_load.return_value = {'currentDateTime': '2023-11-05'}
    result = current_year.what_is_year_now()
    assert result == 2023


@patch('current_year.json.load')
def test_year_dmy_format(mock_json_load):
    mock_json_load.return_value = {'currentDateTime': '05.11.2023'}
    result = current_year.what_is_year_now()
    assert result == 2023


if __name__ == '__main__':  # pragma: no cover
    year = current_year.what_is_year_now()  # pragma: no cover
    print(year)  # pragma: no cover