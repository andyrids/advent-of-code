import functools
import operator
import pathlib

input_txt = pathlib.Path(__file__).parent / "input.txt"

# make the patrol map a list[list[str]]
patrol_map = [list(line) for line in input_txt.read_text().splitlines()]

def get_marker(patrol_map: list[str]) -> tuple[int, int, str]:
    """Get the current marker str and row, column indices.
    
    Args:
        patrol_map (list[str]): List of strings representing map layout.

    Returns:
        Current marker row, column and direction char (<, ^, >, v).
    """

    markers = ("<", ">", "^", "v")
    for i, row in enumerate(patrol_map):
        for j, column in enumerate(row):
            print(column)
            if column not in markers:
                continue
            marker = markers[markers.index(column)]
            return i, j, marker


def advance_marker(
        patrol_map: list[str],
        row: int,
        column: int,
        marker: str
    ) -> tuple[int, int, str] | None:
    """Advance the marker in a direction indicated by the marker parameter.
    If the next position is an obstacle ("#"), then rotate the marker to the
    right and advance.

    Args:
        patrol_map (list[str]): Current mutable patrol map.
        row (int): Current marker row index.
        column (int): Current marker row 'column' index.
        marker (str): Current direction marker.

    Returns:
        The next position row and column indices and direction indicator.
    """

    rotate_marker = {
        "<": "^",
        "^": ">",
        ">": "v",
        "v": "<"
    }

    next_position = {
        "<": (row, column - 1),
        ">": (row, column + 1),
        "^": (row - 1, column),
        "v": (row + 1, column),
    }

    try:
        patrol_map[row][column] = "X"
        new_row, new_column = next_position[marker]
        if patrol_map[new_row][new_column] == "#":
            marker = rotate_marker[marker]
            new_row, new_column = next_position[marker]
    except IndexError:
        # index out of range == end of map
        return None
    else:
        return new_row, new_column, marker

# starting marker position and direction
row, column, marker = get_marker(patrol_map)
while True:
    # next marker position details
    movement = advance_marker(patrol_map, row, column, marker)
    if movement is None:
        break
    # unpack & assign for next advance_marker call
    row, column, marker = movement

# list[list[str]] -> str -> count("X") = positions in patrol
print("".join(["".join(row) for row in patrol_map]).count("X"))