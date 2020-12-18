#!/usr/bin/env python3

## Day 4: Passport Processing

def count_valid_passport():
    count_valid_passport = 0
    passports = []
    passport_string = ''
    with open('input.txt') as file:
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

    #return passports
print(count_valid_passport())
