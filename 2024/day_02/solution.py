import functools
import operator
import pathlib


def reduce_reports(accumulator: list, report: list[str]) -> list[list[int]]:
    """Reduce reports into a list of lists, containing integers
    representing levels.

    Args:
        accumulator (list[list]): Levels in a list of lists.
        report (list[str]): A list of numbers as a string.

    Returns:
        A list of lists containing integers.
    """

    accumulator.append(list(map(int, report)))
    return accumulator


input_txt = pathlib.Path(__file__).parent / "input.txt"

reports = functools.reduce(
    reduce_reports, 
    map(str.split, input_txt.read_text().splitlines()),
    list()
)


def report_filter(report: list[int], dampener: bool = False) -> bool:
    """Filter reports by checking if levels are increasing/decreasing
    by 1-3. If dampener is True, we remove a level from a report list
    and recursively check the levels again, until all iterations have
    failed the check or an iteration passes. This represents tolerating
    a single 'bad' level that prevents the increasing/decreasing by 1-3
    check (part 2).

    Args:
        report (list[int]): List of integers representing levels.
        dampener (bool): Tolerate single 'bad' level flag.

    Returns:
        True if a report levels meet the requirements else False.
    """

    if dampener:
        # indices in current report
        indices = tuple(range(len(report)))
        for idx in indices:
            indexer = operator.itemgetter(*[i for i in indices if i != idx])
            # temp report with all items except current idx (dampener usage)
            temp_report = list(indexer(report))
            # recursive check of temp report
            if report_filter(temp_report):
                return True
        return False
        
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
            # if level check fails and no dampener
            return False
        # all checks passed
        return True

    # report levels are not increasing/decreasing & dampener failed
    return False

print(f"Total reports: {len(reports)}")

# part one safe reports
safe_reports = tuple(filter(report_filter, reports))
print(f"Safe reports (no dampener): {len(safe_reports)}")

dampener_filter = functools.partial(report_filter, dampener=True)
dampener_safe_reports = tuple(filter(dampener_filter, reports))

# 321, 349, 297, 337
print(f"Safe reports (dampener): {len(dampener_safe_reports)}")
