#!/usr/bin/env python3

## Day 3: Toboggan Trajectory

def toboggan():
    # Initialize variables
    matrix = []
    trees = 0
    i = 0
    x = y = 0

    # Create the matrix
    with open('input.txt') as file:
        for line in file:
            matrix.append([])
            for c in line.strip():
                matrix[i].append(c)
            i += 1

    # Calculate tree occurence
    while True:
        x += 1
        if x >= len(matrix):
            break;
        y = (y+3) % len(matrix[x])
        if (matrix[x][y] == '#'):
            trees += 1
    return trees

print(toboggan())
