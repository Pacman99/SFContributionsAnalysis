#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import statistics

props = list(csv.reader(open("../data/sampleProps.csv", "r")))
people = list(csv.reader(open("../data/samplePeople.csv", "r")))

propAmounts = [float(x[1]) for x in props]
peopleAmounts = [float(x[1]) for x in people]

print("Mean for Props:")
print(statistics.mean(propAmounts))
print("Stdev for props:")
print(statistics.pstdev(propAmounts))
print()
print("Mean for people:")
print(statistics.mean(peopleAmounts))
print("Stdev for people:")
print(statistics.pstdev(peopleAmounts))




