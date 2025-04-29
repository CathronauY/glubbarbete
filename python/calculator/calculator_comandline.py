import math

running = True

def calc_add(num1: int, num2: int) -> int:
  answer = num1 + num2
  return answer

def calc_subtract(num1: int, num2: int) -> int:
  answer = num1 - num2
  return answer

def calc_times(num1: int, num2: int) -> int:
  answer = num1 * num2
  return answer

def calc_divide(num1: int, num2: int) -> int:
  answer = num1 / num2
  return answer

while running:
  calculation_type = input("type (add/subtract/times/divide/EXIT): ")
  match calculation_type:
    case "add":
      calculation_type = 1
    case "subtract":
      calculation_type = 2
    case "times":
      calculation_type = 3
    case "divide":
      calculation_type = 4
    case "exit" or "EXIT":
      running = False
    case _:
      exit