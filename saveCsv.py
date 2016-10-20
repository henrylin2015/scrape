#!/usr/bin/env python3
import csv

with open("test.csv", newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print("The album \"{}\" was released in {}".format(str(row[0]),
                                                           str(row[1])))
