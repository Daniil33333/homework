import pytest

from src.masks import get_mask_card_number

# @pytest.fixture()
# def number_16():
#     return ["1234567898765432"
#             ]


def test_get_mask_card_number():
    input_numbers = []
    result = get_mask_card_number("1234567898765432")
    assert result == "1234 56** **** 5432"
# XXXX XX** **** XXXX

# @pytest.mark.parametrize("input_number, expected", [("1234567898765432", "1234 56** **** 5432"),
#                                                     ("12345678987654", pytest.raises(ValueError))])
#
# def test_get_mask_card_number_param(input_number, expected):
#     with pytest.raises(ValueError) as exc_info:
#
#     result = get_mask_card_number(input_number)
#     assert result == expected