# improved version
import pytest

def map_number_to_text(number):
    num_to_text_dict = {
        0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR",
        5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE",
    }
    return num_to_text_dict[number]

def number_as_text(n):
    num_as_text = ""
    remaining_value = n
    while remaining_value > 0:
        remaining_value, remainder = divmod(remaining_value, 10)
        num_as_text = map_number_to_text(remainder) + " "+ num_as_text
    return num_as_text.strip()    
# print(number_as_text(101123456789))
@pytest.mark.parametrize("n, expected",
                         [(7, "SEVEN"),
                          (42, "FOUR TWO"),
                          (7271, "SEVEN TWO SEVEN ONE"),
                          (24680, "TWO FOUR SIX EIGHT ZERO"),
                          (13579, "ONE THREE FIVE SEVEN NINE")])
def test_number_as_text(n, expected):
    assert number_as_text(n) == expected