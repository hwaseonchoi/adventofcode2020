#!/usr/bin/env python3

## Day 2: Password Philosophy

def countValidPassword():
    validPasswordCount = 0
    with open('input.txt') as file:
        for line in file:
            min, max, letter, password = parse(line)
            count = password.count(letter)
            if (count >= min and count <= max):
                validPasswordCount += 1
    return validPasswordCount

def parse(line):
    # example 6-7 z: dqzzzjbzz
    t = line.split(' ')
    minMax = t[0].split('-')
    letter = t[1][0]
    password = t[2]
    return int(minMax[0]), int(minMax[1]), letter, password

print(countValidPassword())
