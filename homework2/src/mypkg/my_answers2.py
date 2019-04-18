#!/usr/bin/python

"""
Python Statements
"""


def add_binary(a, b):
    """
    This is to review binary operations
    ============================================================

    Given two binary strings, return their sum (also a binary string).

    Return None if one of the input strings are empty or contains characters different than 1 or 0.

    Example 1:
                Input: a = "11", b = "1"
                Output: result = "100"

    Example 2:
                Input: a = "1010", b = "1011"
                Output: result = "10101"
    """
    check = ['0','1']
    if bool(a) is False or bool(b) is False:
        return None
    for i in a:
        if not i in check:
            return None
    for i in b:
        if not i in check:
            return None

    # aStr = []
    # aStr.append(a)
    # aStr.append(b)
    # def add(a):
    #     a = '0b' + a
    #     return a
    # aStr = list(map(add,aStr))
    # aInt_dec = []
    # aInt_dec.append(int(aStr[0],2))
    # aInt_dec.append(int(aStr[1],2))
    #
    # result = bin(aInt_dec[0] + aInt_dec[1])
    # result = result[2:]

    a1 = int(a,2)
    a2 = int(b,2)

    result = format(a1+a2,'b')

    return result




    # result = ...
    #
    # return result


def plus_one(digits):
    """
    This is to review loops and if statements
    ============================================================

    Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
    You can do this in-place!

    The digits are stored such that the most significant digit is at the head of the list, and each
    element in the array contain a single digit.

    You may assume the integer does not contain any leading zero, except the number 0 itself.


    Example 1:
            Input: digits = [1, 2, 3]
            Output: digits = [1, 2, 4]
            Explanation: The array represents the integer 123.

    Example 2:
            Input: digits = [1, 0, 9, 9]
            Output: digits = [1, 1, 0, 0]
    """
    carry = 1
    buff = []
    for i in range(len(digits)):
        d = digits.pop()
        d = d + carry
        if d == 10:
            d = 0
            carry = 1
        else:
            carry = 0
        buff.append(d)
    buff.reverse()
    if buff[0] == 0:
        buff.insert(0,1)
    digits = buff
    return digits


def roman_to_integers(roman_string):
    """
    This is to review loops, if statements and dictionaries
    ============================================================

    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    For example, two is written as II in Roman numeral, just two one's added together.
    Twelve is written as, XII, which is simply X + II. The number twenty seven is written
    as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However,
    the numeral for four is not IIII. Instead, the number four is written as IV. Because
    the one is before the five we subtract it making four. The same principle applies to
    the number nine, which is written as IX. There are six instances where subtraction is used:

    - I can be placed before V (5) and X (10) to make 4 and 9.
    - X can be placed before L (50) and C (100) to make 40 and 90.
    - C can be placed before D (500) and M (1000) to make 400 and 900.

    Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

    Example 1:
        Input: "III"
        Output: 3

    Example 2:
        Input: "IV"
        Output: 4

    Example 3:
        Input: "IX"
        Output: 9

    Example 4:
        Input: "LVIII"
        Output: 58
        Explanation: C = 100, L = 50, XXX = 30 and III = 3.

    Example 5:
        Input: "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    r = 0
    for i in range(len(roman_string)-1):
        if dict[roman_string[i]] < dict[roman_string[i+1]]:
            r -= dict[roman_string[i]]
        else:
            r += dict[roman_string[i]]
    integer = r + dict[roman_string[-1]]


    return integer

