# -*- coding: utf-8 -*-
""" Dictionaries used in convert.py,  int_to_roman and roman_to_int """

# these could of just been lists, for speed purposes they are dicts.
INT_TO_ROMAN = {
    1: {1: (1, 'I'),
        2: (2, 'II'),
        3: (3, 'III'),
        4: (4, 'IV'),
        5: (5, 'V'),
        6: (6, 'VI'),
        7: (7, 'VII'),
        8: (8, 'VIII'),
        9: (9, 'IX')},
    2: {1: (10, 'X'),
        2: (20, 'XX'),
        3: (30, 'XXX'),
        4: (40, 'XL'),
        5: (50, 'L'),
        6: (60, 'LX'),
        7: (70, 'LXX'),
        8: (80, 'LXXX'),
        9: (90, 'XC')},
    3: {1: (100, 'C'),
        2: (200, 'CC'),
        3: (300, 'CCC'),
        4: (400, 'CD'),
        5: (500, 'D'),
        6: (600, 'DC'),
        7: (700, 'DCC'),
        8: (800, 'DCCC'),
        9: (900, 'CM')},
    4: {1: (1000, 'M'),
        2: (2000, 'MM'),
        3: (3000, 'MMM')}}

ROMAN_TO_INT = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
    "VIII": 8,
    "IX": 9,
    "X": 10,
    "XX": 20,
    "XXX": 30,
    "XL": 40,
    "L": 50,
    "LXXX": 80,
    "XC": 90,
    "C": 100,
    "CC": 200,
    "CCC": 300,
    "CD": 400,
    "D": 500,
    "DC": 600,
    "DCC": 700,
    "DCCC": 800,
    "CM": 900,
    "M": 1000,
    "MM": 2000,
    "MMM": 3000}

"""
MATH = {
    "I" + "I": "II",
    "II" + "I": "III",
    "V" + "I": "VI",
    "VI" + "I": "VII"
    "X" + "V": "XV"}

    """