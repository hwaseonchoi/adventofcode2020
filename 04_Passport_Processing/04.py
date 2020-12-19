#!/usr/bin/env python3

## Day 4: Passport Processing

import re

def count_valid_passport(input):
    count_valid_passport = 0
    passports = []
    passport_string = ''
    with open(input) as file:
        for line in file:
            if 0 == len(line.strip()):
                passport = parse(passport_string)
                passport_string = ''
                passports.append(passport)
            else:
                passport_string += ' ' + line.strip()
        passport = parse(passport_string)
        passports.append(passport)

    for passport in passports:
        if is_valid(passport):
            count_valid_passport +=1

    return count_valid_passport

def parse(s):
    #pid:831823039 eyr:2028 iyr:2015 ecl:gry hgt:192cm cid:137 byr:1922 hcl:#6b5442
    passport = {}
    if 0 == len(s):
        return passport
    for element in s.split(' '):
        if len(element) == 0:
            continue
        pair = element.split(':')
        passport[pair[0]] = pair[1]
    return passport

def is_valid(passport):
    #byr (Birth Year)
    #iyr (Issue Year)
    #eyr (Expiration Year)
    #hgt (Height)
    #hcl (Hair Color)
    #ecl (Eye Color)
    #pid (Passport ID)
    #cid (Country ID)
    mandatory_attributes = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for attribute in mandatory_attributes:
        if attribute not in passport:
            return False
    return True

def count_valid_passport_2(input):
    count_valid_passport = 0
    passports = []
    passport_string = ''
    with open(input) as file:
        for line in file:
            if 0 == len(line.strip()):
                passport = parse(passport_string)
                passport_string = ''
                passports.append(passport)
            else:
                passport_string += ' ' + line.strip()
        passport = parse(passport_string)
        passports.append(passport)

    for passport in passports:
        if is_valid_2(passport):
            count_valid_passport +=1

    return count_valid_passport

def is_valid_2(passport):
    if not is_valid(passport):
        return False
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
    rules = {
        'byr': ['[0-9]{4}', 1920, 2002],
        'iyr': ['[0-9]{4}', 2010, 2020],
        'eyr': ['[0-9]{4}', 2020, 2030],
        'hgt': ['([0-9]+)(cm|in)', 150, 193],
        'hcl': ['#[0-9a-f]{6}', None, None],
        'ecl': ['(amb|blu|brn|gry|grn|hzl|oth)', None, None],
        'pid': ['[0-9]{9}', None, None]
    }

    for key in rules:
        rule = rules[key]
        pattern, min, max = rule[0], rule[1], rule[2]
        value = passport[key]
        r = re.match(pattern, value)
        if r is not None:
            if len(r.groups()) == 2:
                value = r.group(1)
                unit = r.group(2)
                if unit == 'in':
                    value = float(value)*2.54
            if min is not None and int(value) < min:
                return False
            if max is not None and int(value) > max:
                return False
        else:
            return False
    return True

def test_count_valid_passports():
    assert count_valid_passport('example1.txt') == 2

def test_count_valid_passports_2():
    assert count_valid_passport_2('example2.txt') == 4

def test_resolve():
    print(count_valid_passport('input.txt'))
    print(count_valid_passport_2('input.txt'))
    assert False

    #return passports
print(count_valid_passport('input.txt'))
print(count_valid_passport_2('input.txt'))
