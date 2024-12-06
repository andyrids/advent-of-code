import functools
import operator
import pathlib
import re


def reduce_memory(accumulator: list, memory: list[str]):
    """Reduce memory commands.

    Args:
        accumulator (list[str]): List of command memory strings.
        memory (list[str]): Memory strings.

    Returns:
        List of command memory strings
    """

    accumulator.append("".join(memory))
    return accumulator


def mul(x: int, y: int) -> int:
    """Multiply x and y parameters.

    Args:
        x (int): Integer
        y (int): Integer

    Returns:
        int result of x * y
    """

    return operator.mul(x, y)


input_txt = pathlib.Path(__file__).parent / "input.txt"

memory = functools.reduce(
    reduce_memory, 
    map(str.split, input_txt.read_text().splitlines()),
    list()
)

re_pattern = r"(mul\([0-9]{1,3},[0-9]{1,3}\))"
extract_command = functools.partial(re.findall, re_pattern)

# 1. reduce [["mul(2,2)", "mul(3,5)"], ["mul(2,2)", "mul(3,5)"], ...] 
# 2. eval ["mul(2,2)", "mul(3,5)", "mul(2,2)", "mul(3,5)", ...]
# 3. sum [4, 15, 4, 15]
# 4. 38
commands = map(extract_command, memory)
total = sum(map(eval, functools.reduce(operator.add, commands, list())))

# 180233229
print(total)

re_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)"
extract_command = functools.partial(re.findall, re_pattern)

results = []
enable_commands = True
for command in extract_command(input_txt.read_text()):
    if enable_commands and command.startswith("mul"):
        results.append(eval(command))
        continue
    enable_commands = (False, True)[command == "do()"]

# 95411583
print(sum(results))