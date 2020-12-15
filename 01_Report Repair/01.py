#!/usr/bin/env python3

## Report Repair

def find2020():
    with open('input.txt') as file1:
        for i in file1:
            x = int(i)
            with open('input.txt') as file2:
                for j in file2:
                    y = int(j)
                    if x+y == 2020:
                        return x*y

print(find2020())
