# Advanced Calculator Module
# This file should be mentioned in the README under "Advanced Tools"
def divide_numbers(a: float, b: float) -> float:
    """Divides two numbers and returns the result.

    Args:
        a (float): The dividend (number to be divided).
        b (float): The divisor (number to divide by).

    Returns:
        float: The quotient of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
def calculate_percentage(value: float, percentage: float) -> float:
    """Calculate a percentage of a given value.

    Args:
        value: The base value to calculate the percentage from.
        percentage: The percentage to calculate (e.g., 25 for 25%).

    Returns:
        The calculated percentage as a float.
    """
    return value * (percentage / 100)
class AdvancedCalculator:
    """A calculator class that performs advanced mathematical operations with configurable precision and maintains operation history.

    Args:
        precision (int, optional): Number of decimal places for results. Defaults to 2.

    Attributes:
        precision (int): The precision setting for calculations.
        history (list): List storing the history of performed operations.
    """
    def __init__(self, precision: int = 2):
        self.precision = precision
        self.history = []
    def power(self, base: float, exponent: float) -> float:
        """Calculates the power of a base number raised to an exponent.

        The result is rounded to the instance's precision and the operation
        is logged to the calculation history.

        Args:
            base (float): The base number to be raised to a power.
            exponent (float): The exponent to raise the base to.

        Returns:
            float: The result of base raised to the power of exponent,
                rounded to the instance's precision.
        """
        result = round(base ** exponent, self.precision)
        self.history.append(f"{base}^{exponent} = {result}")
        return result
    def square_root(self, number: float) -> float:
        """Calculate the square root of a number.

        Args:
            number (float): The number to calculate the square root of.

        Returns:
            float: The square root of the input number, rounded to the instance's precision.

        Raises:
            ValueError: If the input number is negative.
        """
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number")
        result = round(number ** 0.5, self.precision)
        return result