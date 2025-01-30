import pytest
import itertools
import numpy as np

# def map_number_to_text(number):
#     num_to_text_dict = {
#         0:"ZERO", 1:"ONE", 2:"TWO", 3:"THREE", 4:"FOUR",
#         5:"FIVE", 6:"SIX", 7:"SEVEN", 8:"EIGHT", 9:"NINE",
#     }
#     return num_to_text_dict[number]

# def number_as_text(n):
#     num_as_text = ""
#     remaining_value = n
#     while remaining_value > 0:
#         remaining_value, remainder = divmod(remaining_value, 10)
#         num_as_text = map_number_to_text(remainder) + " "+ num_as_text
#     return num_as_text.strip()    
# # print(number_as_text(101123456789))
# @pytest.mark.parametrize("n, expected",
#                          [(7, "SEVEN"),
#                           (42, "FOUR TWO"),
#                           (7271, "SEVEN TWO SEVEN ONE"),
#                           (24680, "TWO FOUR SIX EIGHT ZERO"),
#                           (13579, "ONE THREE FIVE SEVEN NINE")])
# def test_number_as_text(n, expected):
#     assert number_as_text(n) == expected

# 2.2.4 optimization
def erase_multiples_of_current(values, number):
    for n in range(number*number, len(values), number):
        values[n] = False

def calc_primes_up_to_max_v2(max_value):
    is_potential_prime = [True for _ in range(1, max_value + 2)]
    for number in range(2, (max_value//2 + 2)):
        if is_potential_prime[number]:
            erase_multiples_of_current(is_potential_prime, number)
    is_potential_prime[0:2] = False, False
    return list(itertools.compress(range(len(is_potential_prime)), is_potential_prime))


def calc_primes_up_to_max_np(max_value):
    arr = np.ones(max_value+1, bool)
    arr[0:2] = False
    for i in range(len(arr)):
        if arr[i]:
            arr[i*i::i] = False
            # print(i, arr)
    return list(np.flatnonzero(arr))

def input_and_expected():
    return [
        (2, [2]),
        (3, [2, 3]),
        (10, [2, 3, 5, 7]),
        (15, [2, 3, 5, 7, 11, 13]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (25, [2, 3, 5, 7, 11, 13, 17, 19, 23]),
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
    ]

# @pytest.mark.parametrize("n, expected", input_and_expected())
# def test_cal_prime_numbers(n, expected):
#     assert calc_primes_up_to_max_v2(n) == expected

# @pytest.mark.parametrize("n, expected", input_and_expected())
# def test_cal_prime_numbers_using_np(n, expected):
#     assert calc_primes_up_to_max_np(n) == expected

def calc_checksum(digits: str):
    if not digits.isdigit():
        raise ValueError("illegal chars: not only digits!")
    check_sum = [(n[0]+1)*int(n[1]) for n in enumerate(digits)]
    return sum(check_sum) % 10

@pytest.mark.parametrize("n, expected", 
                         [("11111", 5),
                          ("22222", 0),
                          ("111111", 1),
                          ("12345678", 4),
                          ("87654321", 0)])
def test_cal_checksum(n,expected):
    assert calc_checksum(n) == expected
def test_calc_checksum_with_letters_as_wrong_input():
    with pytest.raises(ValueError) as excinfo:
        calc_checksum("ABC")
    assert "illegal chars" in str(excinfo.value)