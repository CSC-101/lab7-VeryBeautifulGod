import sys
from typing import Optional

def str_to_float(s: str) -> Optional[float]:
    try:
        return float(s)
    except ValueError:
        return None

def sum_command_line_arguments() -> float:
    total = 0.0
    for arg in sys.argv[1:]:
        number = str_to_float(arg)
        if number is not None:
            total += number
    return total

if __name__ == '__main__':
    total_sum = sum_command_line_arguments()
    print("Sum of command-line arguments:", total_sum)

