#test_file.py

def add_numbers(a, b): 
  return a + b 

def multiply(x, y): 
  result = x * y 
  return result 

class Calculator: 
  def divide(self, a, b): 
    if b == 0: 
      raise ValueError("Cannot divide by zero") 
    return a / b
