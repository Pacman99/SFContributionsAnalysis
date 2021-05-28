#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import random

sampleSize = 32

props = list(csv.reader(open("../data/props.csv", "r")))
people = list(csv.reader(open("../data/people.csv", "r")))

sampleProps = csv.writer(open("../data/sampleProps.csv", "w+"))
samplePeople = csv.writer(open("../data/samplePeople.csv", "w+"))

propsNums = list(range(len(props)))
peopleNums = list(range(len(people)))

for num in range(sampleSize):
    propNum = random.choice(propsNums)
    print(propNum)
    propsNums.remove(propNum)
    peopleNum = random.choice(peopleNums)
    print(peopleNum)
    peopleNums.remove(peopleNum)

    sampleProps.writerow(props[propNum])
    samplePeople.writerow(people[peopleNum])


