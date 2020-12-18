#!/usr/bin/env python3

## Day 3: Toboggan Trajectory

def toboggan(right = 3, down =1):
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
        x += down
        if x >= len(matrix):
            break;
        y = (y+right) % len(matrix[x])
        if (matrix[x][y] == '#'):
            trees += 1
    return trees

print(toboggan())

product = 1
for pair in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    print(pair)
    product *= toboggan(pair[0], pair[1])
print(product)
