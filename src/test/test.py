# import src.assignments
from assignment_1 import *


def test_is_valid_phone_number():
    phone_n = ''
    is_valid = is_valid_phone_number(phone_n)
    assert is_valid == False, f"{phone_n} failed"

    phone_n = '123'
    is_valid = is_valid_phone_number(phone_n)
    assert is_valid == False, f"{phone_n} failed"

    phone_n = '+911234567891'
    is_valid = is_valid_phone_number(phone_n)
    assert is_valid == True, f"{phone_n} failed"

    phone_n = '+1 212.456.7890'
    is_valid = is_valid_phone_number(phone_n)
    assert is_valid == True, f"{phone_n} failed"

    phone_n = '212-456-7890'
    is_valid = is_valid_phone_number(phone_n)
    assert is_valid == True, f"{phone_n} failed"

    phone_n = '(212)-456-7890'
    is_valid = is_valid_phone_number(phone_n)
    assert is_valid == True, f"{phone_n} failed"

if __name__ == '__main__':
    test_is_valid_phone_number()