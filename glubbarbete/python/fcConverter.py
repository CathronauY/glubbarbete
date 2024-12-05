def FToC():
    fahrenheit = int(input("Input fahrenheit and ill convert it to celsius: "))
    celsius = (fahrenheit - 32) / 1.8
    print(f"Celsius: {celsius:.2f} ")

def CToF():
    celsius = int(input("Input celsius and ill convert it to fahrenheit: "))
    fahrenheit = (celsius * 1.8) + 32
    print(f"Fahrenheit: {fahrenheit:.2f}")

opt = input("Fahrenheit or Celsius: ")

while(opt != "Fahrenheit" and opt != "Celsius"): 
    opt = int(input("Invalid input, please try again: "))

if(opt == "Fahrenheit"): FToC()
else: CToF()
