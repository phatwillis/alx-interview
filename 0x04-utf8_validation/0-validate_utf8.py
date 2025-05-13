#!/usr/bin/python3
"""a method that determines if a given data set
represents a valid UTF-8 encoding."""


def validUTF8(data):
    """
    validates a data set. each number in the data set
    represents a byte, so will be converted to binary.
    if a character is just a byte long, it starts with just 0.
    for multibyte characters:
    - For characters encoded with two bytes, the first byte must
    start with the bit pattern "110".
    - For characters encoded with three bytes, the first byte must
    start with the bit pattern "1110".
    - For characters encoded with four bytes, the first byte must
    start with the bit pattern "11110".

    refer to utf-8 on wikipedia, header: FSS-UTF (1992) / UTF-8 (1993)
    to remember.
    or Characters, Symbols and the Unicode Miracle - Computerphile on youtube
    from the 6th minute
    """

    if data == []:  # if data is an empty list
        return True

    # create a list with the binary versions of the numbers in the data set.
    # [2:] slices the initial 0b used to specify the number is a binary
    # zfill is used to fill the numbers with 0's to complete the 8-bit byte
    binary_data = [bin(num)[2:].zfill(8) for num in data]
    # check if the first binary num starts with 0.
    # 0 is written as string because slice returns a string.
    if binary_data[0][0:1] == "0":
        return True  # because it is a data set of single byte characters
    # if it is multibyte, ensure it follows multibyte rules
    elif binary_data[0][0:3] == "110" \
            or binary_data[0][0:4] == "1110" and len(binary_data) >= 3 \
            or binary_data[0][0:5] == "11110" and len(binary_data) >= 4:
        # if it is 2 bytes long and above:
        for bin_num in binary_data[1:]:
            if bin_num[0:2] != "10":  # ensure subsequent bytes start with 10
                return False
        return True  # return true if rules are followed.
    else:  # all utf-validations failed
        return False
