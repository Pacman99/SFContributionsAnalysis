#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

population = csv.reader(open("../data/population.csv", "r"))
props = csv.writer(open("../data/props.csv", "w+"))
people = csv.writer(open("../data/people.csv", "w+"))

matches = [
    "yes on",
    "no on",
    "prop",
]
def checkForProp(committee):
    for text in matches:
        if text in committee:
            return True

    return False

for line in population:
    committee = line[2].lower()
    if checkForProp(committee):
        props.writerow(line)
    elif " for " in committee:
        people.writerow(line)
