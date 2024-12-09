import functools
import math
import operator
import pathlib
import statistics

from collections import defaultdict


input_txt = pathlib.Path(__file__).parent / "input.txt"

rules, *_, pages = input_txt.read_text().partition("\n\n")

middle_number_total = 0
for page in pages.splitlines():
    try:
        page_numbers = page.split(",")
        for rule in rules.splitlines():
            before, after = rule.split("|")
            if before in page_numbers and after in page_numbers:
                if page.index(before) > page.index(after):
                    raise ValueError
    except ValueError:
        continue
    else:
        middle = statistics.median(range(len(page_numbers)))
        middle_number_total += int(page_numbers[middle])

           
# 12667 (high) | 18300 (high) | 4185
print(middle_number_total)