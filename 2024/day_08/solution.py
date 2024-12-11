import functools
import itertools
import operator
import pathlib
import re


input_txt = pathlib.Path(__file__).parent / "input.txt"

frequencies = re.finditer(r"([A-Z0-9])", input_txt.read_text(), re.IGNORECASE)

unique_frequencies = set(map(operator.methodcaller("group"), frequencies))

print(input_txt.read_text())

