import functools
import operator
import pathlib


input_txt = pathlib.Path(__file__).parent / "input.txt"

def reduce_lists(accumulator: tuple[list, list], numbers: list[str]):
    """Reduce a list of strings containing space-separated numbers
    into a tuple containing two lists.

    For example:

    ["11111", "22222"] -> ([11111], [22222])
    ["33333", "44444"] -> ([11111, 33333], [22222, 44444])

    Args:
        accumulator (tuple[list, list]): Accumulator for number strings
        numbers (str): A string containing space separated numbers

    Returns:
        tuple with two lists
    """

    for idx, number in enumerate(numbers):
        accumulator[idx].append(int(number))
    return accumulator

input_lists = functools.reduce(
    reduce_lists, 
    map(str.split, input_txt.read_text().splitlines()),
    ([],[])
) 

def subtract(items: tuple[int]) -> int:
    """Absolute difference between two integers."""

    return abs(operator.sub(*items))

sorted_lists = tuple(map(sorted, input_lists))
result = sum(map(subtract, zip(*sorted_lists)))

(left, right) = sorted_lists
similarity_score = sum([number * right.count(number)  for number in left])