# Python calculator

# Add
def add(n1, n2):
  """Adds two numbers n1 and n2"""
  return n1 + n2

# Subtract
def subtract(n1, n2):
  """Subtracts n2 from n1"""
  return n1 - n2

# Multiply
def multiply(n1, n2):
  """Multiply n1 by n2"""
  return n1 * n2

# Divide
def divide(n1, n2):
  """Divide n1 by n2"""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What is the first number?: "))

for operator in operations:
  print(operator)

symbol = input("Pick an operator from the line above: ")

num2 = int(input("What is the second number?: "))

answer = operations[symbol](num1, num2)

print(f"{num1} {symbol} {num2} = {answer}")