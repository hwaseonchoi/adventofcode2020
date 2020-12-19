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

def find_my_seat(input):
    seats = []
    with open(input) as file:
        for line in file:
            seats.append(convert(line.strip()))

    seats.sort()
    previous_seat = None
    for seat in seats:
        if previous_seat is None:
            previous_seat = seat
            continue
        if seat - previous_seat > 1:
            return seat - 1
        previous_seat = seat

def convert(s):
    row_string = s[0:7]
    column_string = s[7:10]
    row = int(row_string.replace('F', '0').replace('B', '1'), 2)
    col = int(column_string.replace('L', '0').replace('R', '1'), 2)

    return row*8+col

#test
def test_converter():
    assert convert('BBBBBBBRRR') == 1023

def test_resolve():
    print('convert BBBBBBBRRR:', convert('BBBBBBBRRR'))
    print('highest seat', highest_seat())
    print('my seat', find_my_seat('input.txt'))
    assert False, 'solutions'
