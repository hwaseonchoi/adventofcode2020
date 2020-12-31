#!/usr/bin/env python3

## Day 8: Handy Haversacks

import re

class Code:
    def __init__(self, input):
        self.instructions = []
        self.acc = 0
        self.cursor = 0
        self.status = 'running'
        self.parse(input)

    def parse(self, filename):
        # nop +0
        # acc +1
        # jmp +4
        # acc +3
        # jmp -3
        # acc -99
        # acc +1
        # jmp -4
        # acc +6
        with open(filename) as file:
            for line in file:
                self.instructions.append(line.strip())
    def run(self):
        seen_instructions = set()
        while True:
            self.next()
            if self.cursor in seen_instructions:
                return 1
            seen_instructions.add(self.cursor)
            if self.status == 'terminated':
                return 0
    def increment_cursor(self, n):
        self.cursor += n
        if self.cursor == len(self.instructions):
            self.status = 'terminated'

    def next(self):
        """
            Execute the instruction
        """
        instruction = self.instructions[self.cursor]
        self.execute(instruction)

    def execute(self, instruction):
        if self.status == 'terminated':
            return

        r = re.match('^([a-z]{3}) (.*)', instruction)
        i = r.group(1)
        n = int(r.group(2))

        if i == 'nop':
            self.increment_cursor(1)
        elif i == 'jmp':
            self.increment_cursor(n)
        elif i == 'acc':
            self.acc += n
            self.increment_cursor(1)

    def reset(self):
        self.cursor = 0
        self.acc = 0

    def revert(self, i):
        instruction = self.instructions[i]
        if 'jmp' in instruction:
            self.instructions[i] = instruction.replace('jmp', 'nop')
            print('instr', instruction, 'jmp -> nop')
        elif 'nop' in instruction:
            self.instructions[i] = instruction.replace('nop', 'jmp')
            print('instr', instruction, 'nop -> jmp')
        else:
            return 1
        return 0

def detect_loop(input):
    code = Code(input)
    code.run()
    return code.acc

def correct_loop(input):
    code = Code(input)
    for i in range(0, len(code.instructions)):
        code.revert(i)
        code.run()
        print(code.status, code.cursor, code.acc)
        if code.status == 'terminated':
            return code.acc
        code.revert(i)
        code.reset()


def test_example1():
    assert detect_loop('example1.txt') == 5
def test_example2():
    assert correct_loop('example1.txt') == 8

def test_resolve():
    print(detect_loop('input.txt'))
    assert detect_loop('input.txt') == 1797
    print(correct_loop('input.txt'))
    assert False
