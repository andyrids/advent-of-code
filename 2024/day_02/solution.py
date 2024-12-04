import functools
import math
import operator
import pathlib


def reduce_reports(accumulator: list, report: str) -> list[tuple]:
    """

    Args:
        accumulator (list[tuple]): 
        numbers (str): 

    Returns:
        
    """

    accumulator.append(list(map(int, report)))
    return accumulator


input_txt = pathlib.Path(__file__).parent / "input.txt"

reports = functools.reduce(
    reduce_reports, 
    map(str.split, input_txt.read_text().splitlines()),
    list()
)


def report_filter(report: list[int]) -> bool:
    """

    Args:
        report (list[int]):

    Returns:
        bool
    """

    increasing = sorted(report, reverse=False)
    decreasing = sorted(report, reverse=True)

    # are report levels increasing or decreasing
    if report == increasing or report == decreasing:
        # doesn't matter if we use increasing or decreasing
        # the absolute difference will be the same
        while len(decreasing) > 1:
            # we pop the first item and max returns the next
            difference = decreasing.pop(0) - max(decreasing)
            if 0 < difference <= 3:
                continue
            # if level check fails
            return False
        # all checks passed
        return True
    # report levels are not increasing or decreasing
    return False




print(len(tuple(filter(report_filter, reports))))

