import functools
import operator
import pathlib
import re


def get_count(text: str) -> int:
    """Count occurrences of 'XMAS'|'SAMX' in text.
    
    Args:
        text (str): String to search.
    
    Returns:
        Number of matches for both search options.
    """
    
    return len(re.findall(r"XMAS", text) + re.findall(r"SAMX", text))


input_txt = pathlib.Path(__file__).parent / "input.txt"

word_search = input_txt.read_text().splitlines()

rows, columns = len(word_search), len(word_search[0])

search_count = 0
for row in word_search:
    search_count += get_count(row)

for column in range(columns):
    column_text = ""
    for row in range(rows):
        column_text += word_search[row][column]
    search_count += get_count(column_text)

for left_diagonal in range(rows + columns - 1):
    diagonal_text = ""
    for row in range(rows):
        column = left_diagonal - row
        if 0 <= column < columns:
            diagonal_text += word_search[row][column]
    search_count += get_count(diagonal_text)

for right_diagonal in range(rows + columns - 1):
    diagonal_text = ""
    for row in range(rows):
        column = (columns - 1) - (right_diagonal - row)
        if 0 <= column < columns:
            diagonal_text += word_search[row][column]
    search_count += get_count(diagonal_text)

# 1654 (low) | 1766 (low) | 2613
print(search_count)


cross_count = 0
for row in range(1, len(word_search)-1):
    for column in range(1, len(word_search[0])-1):
        if word_search[row][column] == "A":
            diagonal_left = "".join(
                [
                    word_search[row - 1][column - 1],
                    "A",
                    word_search[row + 1][column + 1]
                ]
            )

            diagonal_right = "".join(
                [
                    word_search[row - 1][column + 1],
                    "A",
                    word_search[row + 1][column - 1]
                ]
            )

            if (
                diagonal_left in ("MAS", "SAM") and
                diagonal_right in ("MAS", "SAM")
            ):
                cross_count += 1
print(cross_count)
