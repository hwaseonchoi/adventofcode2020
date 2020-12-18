#!/usr/bin/env python3

## Report Repair

def find2020():
    with open('input.txt') as file:
        for i in file:
            x = int(i)
            with open('input.txt') as file2:
                for j in file2:
                    y = int(j)
                    if x+y == 2020:
                        return x*y

def find2020_2():
    with open('input.txt') as file:
        for i in file:
            x = int(i)
            with open('input.txt') as file2:
                for j in file2:
                    y = int(j)
                    with open('input.txt') as file3:
                        for k in file3:
                            z = int(k)
                            if x+y+z == 2020:
                                return x*y*z

print(find2020())
print(find2020_2())
