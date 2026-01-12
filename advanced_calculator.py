# Advanced Calculator Module
# This file should be mentioned in the README under "Advanced Tools"
def divide_numbers(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
def calculate_percentage(value: float, percentage: float) -> float:
    return value * (percentage / 100)
class AdvancedCalculator:
    def __init__(self, precision: int = 2):
        self.precision = precision
        self.history = []
    def power(self, base: float, exponent: float) -> float:
        result = round(base ** exponent, self.precision)
        self.history.append(f"{base}^{exponent} = {result}")
        return result
    def square_root(self, number: float) -> float:
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = round(number ** 0.5, self.precision)
        return result
