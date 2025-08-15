# Unit Converter Project (Length, Weight, Temperature)

def length_converter():
    print("\nLength Conversion:")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Meters to Miles")
    print("4. Miles to Meters")
    choice = int(input("Choose an option: "))

    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value} meters = {value / 1000} kilometers")
    elif choice == 2:
        print(f"{value} kilometers = {value * 1000} meters")
    elif choice == 3:
        print(f"{value} meters = {value / 1609.34:.4f} miles")
    elif choice == 4:
        print(f"{value} miles = {value * 1609.34:.2f} meters")
    else:
        print("Invalid choice!")


def weight_converter():
    print("\nWeight Conversion:")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")
    choice = int(input("Choose an option: "))

    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value} kg = {value * 1000} grams")
    elif choice == 2:
        print(f"{value} grams = {value / 1000} kg")
    elif choice == 3:
        print(f"{value} kg = {value * 2.20462:.2f} pounds")
    elif choice == 4:
        print(f"{value} pounds = {value / 2.20462:.2f} kg")
    else:
        print("Invalid choice!")


def temperature_converter():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = int(input("Choose an option: "))

    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value}°C = {(value * 9/5) + 32}°F")
    elif choice == 2:
        print(f"{value}°F = {(value - 32) * 5/9}°C")
    elif choice == 3:
        print(f"{value}°C = {value + 273.15} K")
    elif choice == 4:
        print(f"{value} K = {value - 273.15}°C")
    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        option = int(input("Choose category: "))

        if option == 1:
            length_converter()
        elif option == 2:
            weight_converter()
        elif option == 3:
            temperature_converter()
        elif option == 4:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option! Please choose again.")


if __name__ == "__main__":
    main()
