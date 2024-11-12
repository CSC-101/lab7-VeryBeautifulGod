from typing import List, Optional

def str_to_float(s: str) -> Optional[float]:
    try:
        return float(s)
    except ValueError:
        return None

def gather_numbers() -> List[float]:
    numbers = []
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == "done":
            break
        number = str_to_float(user_input)
        if number is not None:
            numbers.append(number)
    return numbers

if __name__ == '__main__':
    numbers = gather_numbers()
    print("Sum of numbers:", sum(numbers))

