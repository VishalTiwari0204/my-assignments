#
# This file implements assignments given by ful.io
# Date Created: 26-Nov-2022 
# Last Updated: 26-Nov-2022
# Author : Vishal Tiwari 

# Assignments: It is available in doc/
# References:
# 1. https://en.wikipedia.org/wiki/List_of_country_calling_codes#:~:text=Country%20codes%20are%20a%20component%20of%20the%20international,also%20indicates%20to%20the%20subscriber%20that%20the%20local

import re



PHONE_NUMBERS = [
        '2124567890',
        '212-456-7890',
        '(212)456-7890',
        '(212)-456-7890',
        '212.456.7890',
        '212 456 7890',
        '+12124567890',
        '+12124567890',
        '+1 212.456.7890',
        '+212-456-7890',
        '1-212-456-7890']

def is_valid_phone_number(phone_number):
    """ This function tells if the phone number is valid
    Arguments:
        phone_number (str) phone number to be validated
    
    Returns:
        True if given phone number is valid otherwise False
    """
    # standard format of phone number:
    #       [+][country code][area code][local phone number]
    
    pattern = re.compile("[+]?\d{0,3}[\s]?[(]?\d{3}[)]?[-\s\.]?\d{3}[-\s\.]?\d{4}")
    output = re.findall(pattern, phone_number)



    # print(output)
    is_valid = False
    if len(output):
        is_valid = True

    return is_valid

def process_phone_numbers():
    """ Wrapper fnction to test list of numbers
    Arguments:
        None
    
    Returns:
        None
    """
    result = {}
    for pn in PHONE_NUMBERS:
        is_valid = is_valid_phone_number(pn)
        result[pn] = is_valid
    
    print(result)


# cmd = ["whois", "ful.io"]
if __name__ == '__main__':
    process_phone_numbers()
    

