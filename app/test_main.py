import pytest

from app.main import get_coin_combination


@pytest.mark.parametrize(
    "cents,combination",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_should_return_the_combination(
        cents: int,
        combination: list
) -> None:
    result = get_coin_combination(cents)
    assert result == combination
