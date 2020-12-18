#!/usr/bin/env python3

## Day 2: Password Philosophy

def count_valid_password():
    valid_password_count = 0
    with open('input.txt') as file:
        for line in file:
            min, max, letter, password = parse(line)
            count = password.count(letter)
            if (count >= min and count <= max):
                valid_password_count += 1
    return valid_password_count

def count_valid_password_2():
    valid_password_count = 0
    with open('input.txt') as file:
        for line in file:
            pos1, pos2, letter, password = parse(line)
            b1 = password[pos1-1] == letter
            b2 = password[pos2-1] == letter
            #(a and not b) or (not a and b)
            if (b1^b2):
                valid_password_count +=1
    return valid_password_count

def parse(line):
    # example 6-7 z: dqzzzjbzz
    t = line.split(' ')
    min_max = t[0].split('-')
    letter = t[1][0]
    password = t[2]
    return int(min_max[0]), int(min_max[1]), letter, password

print(count_valid_password())
print(count_valid_password_2())
