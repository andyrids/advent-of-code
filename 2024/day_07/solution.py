import functools
import itertools
import operator
import pathlib

input_txt = pathlib.Path(__file__).parent / "input.txt"

def solve_equation(numbers: list[int], target):
    """Determine if target can be achieved by inserting +/* between nums.
    
    Args:
        numbers (list[int]): Numbers in the equation.
        target (int): Target value to match.
    
    Returns:
        bool: True if equation can be solved, False otherwise.
    """
    def evaluate(numbers, operators):
        """Evaluate the expression left-to-right."""
        result = numbers[0]
        for i in range(len(operators)):
            if operators[i] == "+":
                result += numbers[i+1]
            elif operators[i] == "*":
                result *= numbers[i+1]
            else:
                result = int(f"{result}{numbers[i+1]}")
        return result
    

    
    # We need len(nums) - 1 operators
    operator_count = len(numbers) - 1
    
    # Try all combinations of '+' and '*'
    for operators in itertools.product(['+', '*', "||"], repeat=operator_count):
        if evaluate(numbers, operators) == target:
            return True
    
    return False

def total_calibration_result(equations: list[str]):
    """Calculate the total calibration result.
    
    Args:
        equations (list[str]): List of equation strings.
    
    Returns:
        int: Sum of test values for solvable equations.
    """
    total = 0
    for equation in equations:
        # Split the equation into test value and numbers
        test_value, num_str = equation.split(': ')
        test_value = int(test_value)
        nums = list(map(int, num_str.split()))
        
        # Check if the equation is solvable
        if solve_equation(nums, test_value):
            total += test_value
    
    return total


# 229926 (low) | 133867379 (low) | 7133867379 (low) 
# 2299996598920 (high) | 2299996598890
print(total_calibration_result(input_txt.read_text().splitlines()))

# 362646859298554 (with "||" added to solve_equation)
print(total_calibration_result(input_txt.read_text().splitlines()))