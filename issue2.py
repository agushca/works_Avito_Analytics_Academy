import pytest
from issue1 import decode


@pytest.mark.parametrize('input, expected_output', [
    ('... --- ...', 'SOS'),
    ('.... . .-.. .-.. ---', 'HELLO'),
    ('.. -.. .. -.. .. -', 'IDIDIT'),
])
def test_decode(input, expected_output):
    """Проверка для верного кодирования"""
    assert decode(input) == expected_output


if __name__ == '__main__':
    pytest.main()