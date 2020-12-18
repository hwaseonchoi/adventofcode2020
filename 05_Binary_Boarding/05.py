#!/usr/bin/env python3

## Day 5: Binary Boarding

def highest_seat():
    with open('input.txt') as file:
        id_max = 0
        for line in file:
            id = convert(line.strip())
            if id > id_max:
                id_max = id
        return id_max

def convert(s):
    row_string = s[0:7]
    column_string = s[7:10]
    row = int(row_string.replace('F', '0').replace('B', '1'), 2)
    col = int(column_string.replace('L', '0').replace('R', '1'), 2)

    return row*8+col

print(convert('BBBBBBBRRR')) #test
print(highest_seat())
