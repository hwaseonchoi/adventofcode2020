#!/usr/bin/env python3

## Day 6: Custom Customs

def count_yes(input):
    answered_questions = ''
    sum = 0

    with open(input) as file:
        for line in file:
            if line == '\n':
                sum += len(set([e for e in answered_questions]))
                answered_questions = ''
            else:
                answered_questions += line.strip()

    sum += len(set([e for e in answered_questions]))

    return sum

def count_everyone_answers_yes(input):
    answered_questions = ''
    sum = 0
    questions = None
    with open(input) as file:
        for line in file:
            if line == '\n':
                sum += len(questions)
                questions = None
            else:
                answered_questions = set([e for e in line.strip()])
                print(answered_questions)
                if questions is None:
                    questions = answered_questions
                else:
                    questions = questions.intersection(answered_questions)
                print(questions)

    sum += len(questions)

    return sum

print(count_everyone_answers_yes('input.txt'))
print(count_yes('input.txt'))

def test_count_everyone_answers_yes():
    assert count_everyone_answers_yes('example1.txt') == 6
