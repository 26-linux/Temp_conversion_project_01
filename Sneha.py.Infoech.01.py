def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("Choose the original unit:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    choice = input("Enter 1, 2, or 3: ")
    temperature = float(input("Enter the temperature value: "))

    if choice == '1':
        print(f"{temperature} °C is equal to {celsius_to_fahrenheit(temperature):.2f} °F and {celsius_to_kelvin(temperature):.2f} K.")
    elif choice == '2':
        print(f"{temperature} °F is equal to {fahrenheit_to_celsius(temperature):.2f} °C and {fahrenheit_to_kelvin(temperature):.2f} K.")
    elif choice == '3':
        print(f"{temperature} K is equal to {kelvin_to_celsius(temperature):.2f} °C and {kelvin_to_fahrenheit(temperature):.2f} °F.")
    else:
        print("Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()
