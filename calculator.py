# This file contains mathematical utility functions
# Note: This file should be mentioned in the README under a "Utilities" section
def add_numbers(a, b):
    return a + b
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Dimensions must be positive")
    return length * width
def find_maximum(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val
class Calculator:
    def __init__(self):
        self.history = []
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    def get_history(self):
        return self.history.copy()
