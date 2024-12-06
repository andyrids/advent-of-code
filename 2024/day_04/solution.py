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