def FahrenheitToCelsius() -> int:
    fahrenheit = int(input("Input fahrenheit and ill convert it to celsius: "))
    celsius = (fahrenheit - 32) / 1.8
    return celsius

def CelsiusToFahrenheit() -> int:
    celsius = int(input("Input celsius and ill convert it to fahrenheit: "))
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

opt = input("Fahrenheit or Celsius: ")

while(opt != "Fahrenheit" and opt != "Celsius"): 
    opt = input("Invalid input, please try again: ")

if(opt == "Fahrenheit"):
    answer = FahrenheitToCelsius()
    print(answer)
else:
    answer = CelsiusToFahrenheit()
    print(answer)
