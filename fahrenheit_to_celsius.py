import sys

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fahrenheit_to_celsius.py <temperature_in_fahrenheit>")
        sys.exit(1)

    # Convert the argument to a float
    try:
        fahrenheit = float(sys.argv[1])
    except ValueError:
        print("Please provide a valid number for the temperature in Fahrenheit.")
        sys.exit(1)

    # Convert to Celsius
    celsius = fahrenheit_to_celsius(fahrenheit)
    
    # Display the result
    print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")


