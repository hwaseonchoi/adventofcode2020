#!/usr/bin/env python3

## Day 7: Handy Haversacks

import re

def parse_rules(input):
    {
        'shiny gold': set(['bright white', 'muted yellow']),
        'muted yellow': set(['dark orange']),
    }
    container_bags = {}
    {
        'shiny gold': {'dark green': 2, 'fuchsia': 2, 'tomato': 1},
    }
    bag_contents = {}
    with open(input) as file:
        for line in file:
            # drab brown bags contain 2 dark green bags, 2 plaid fuchsia bags, 1 muted tomato bag, 5 light tan bags.
            # faded blue bags contain no other bags.
            p1 = '^(.*) bags contain (.*)'
            p2 = '([0-9]+) (.*) bags?'
            p3 = '^(.*) bags contain no other bags.'
            r1 = re.match(p1, line)

            if r1 is not None:
                super_bag = r1.group(1)
                if super_bag not in bag_contents:
                    bag_contents[super_bag] = dict()
                bags_str = r1.group(2)
                for bag_str in bags_str.split(', '):
                    r2 = re.match(p2, bag_str)
                    if r2 is not None:
                        bag = r2.group(2)
                        number = int(r2.group(1))
                        if bag not in container_bags:
                            container_bags[bag] = set()
                        container_bags[bag].add(super_bag)
                        bag_contents[super_bag][bag] = number

        return container_bags, bag_contents

def count_bags(input):
    container_bags, bag_contents = parse_rules(input)
    shiny_gold_bags = container_bags['shiny gold']
    while True:
        before = len(shiny_gold_bags)
        for bag in shiny_gold_bags:
            if bag in container_bags:
                shiny_gold_bags = shiny_gold_bags.union(container_bags[bag])
        after = len(shiny_gold_bags)

        if before == after:
            break

    return len(shiny_gold_bags)

def count_contained_bags(input):
    container_bags, bag_contents = parse_rules(input)
    return count_contained_bags_recursive('shiny gold', bag_contents)

def count_contained_bags_recursive(bag, bag_contents):
    {
        'shiny gold': {'dark green': 2, 'fuchsia': 2, 'tomato': 1},
    }
    sum = 0
    contents = bag_contents[bag]
    for subbag in contents:
        number = contents[subbag]
        sum += number + number * count_contained_bags_recursive(subbag, bag_contents)

    return sum

def test_example1():
    assert count_bags('example1.txt') == 4
def test_example2():
    assert count_contained_bags('example2.txt') == 126

def test_resolve():
    print(count_bags('input.txt'))
    print(count_contained_bags('input.txt'))
    assert False
