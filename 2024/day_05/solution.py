import functools
import math
import operator
import pathlib
import statistics

from collections import defaultdict


input_txt = pathlib.Path(__file__).parent / "input.txt"

rules, *_, pages = input_txt.read_text().partition("\n\n")

incorrect_pages = []
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
        incorrect_pages.append(page_numbers)
        continue
    else:
        middle = statistics.median(range(len(page_numbers)))
        middle_number_total += int(page_numbers[middle])

# 12667 (high) | 18300 (high) | 4185
print(middle_number_total)


def reorder_pages(pages: list[int]) -> list[int]:
    """Reorder pages based on page order rules."""

    changes = False
    for rule in rules.splitlines():
        before, after = rule.split("|")
        if (before in pages) and (after in pages):
            if (i := pages.index(before)) > (j := pages.index(after)):
                pages[i], pages[j] = pages[j], pages[i]
                changes = True
    return changes


middle_corrected_total = 0
for pages in incorrect_pages:
    while reorder_pages(pages):
        pass
    middle_corrected_total += int(pages[len(pages) // 2])

print(middle_corrected_total)