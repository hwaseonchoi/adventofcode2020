#!/usr/bin/env python3

## Day 6: Custom Customs

def count_yes():
    answered_questions = ''
    sum = 0

    with open('input.txt') as file:
        for line in file:
            if line == '\n':
                sum += len(set([e for e in answered_questions]))
                answered_questions = ''
            else:
                answered_questions += line.strip()

    sum += len(set([e for e in answered_questions]))
    
    return sum

print(count_yes())
