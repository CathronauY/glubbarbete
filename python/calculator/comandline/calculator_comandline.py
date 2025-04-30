def calc_add(num1: int, num2: int) -> int:
  """
  num1: int
  num2: int
  return: num1 + num2
  """
  answer = num1 + num2
  return answer

def calc_subtract(num1: int, num2: int) -> int:
  """
  num1: int
  num2: int
  return: num1 - num2
  """
  answer = num1 - num2
  return answer

def calc_times(num1: int, num2: int) -> int:
  """
  num1: int
  num2: int
  return: num1 * num2
  """
  if num1 == 0 or num2 == 0:
    answer = 0
  else:
    answer = num1 * num2
  return answer

def calc_divide(num1: int, num2: int) -> int:
  """
  num1: int
  num2: int
  return: num1 / num2
  """
  if num1 == 0 or num2 == 0:
    answer = 0
  else:
    answer = num1 / num2
  return answer

def main() -> None:
  while running:
    calculation_type: int = input("type (add/subtract/times/divide/EXIT): ").lower()
    match calculation_type:
      case "add":
        calculation_type = 1
      case "subtract":
        calculation_type = 2
      case "times":
        calculation_type = 3
      case "divide":
        calculation_type = 4
      case "exit":
        running = False
      case _:
        exit

    if calculation_type == 1:
      num1: int = int(input("nummer 1: "))
      num2: int = int(input("nummer 2: "))
      print(calc_add(num1, num2))
    elif calculation_type == 2:
      num1: int = int(input("nummer 1: "))
      num2: int = int(input("nummer 2: "))
      print(calc_subtract(num1, num2))
    elif calculation_type == 3:
      num1: int = int(input("nummer 1: "))
      num2: int = int(input("nummer 2: "))
      print(calc_times(num1, num2))
    elif calculation_type == 4:
      num1: int = int(input("nummer 1: "))
      num2: int = int(input("nummer 2: "))
      print(calc_divide(num1, num2))

if __name__ == "__main__":
  main()