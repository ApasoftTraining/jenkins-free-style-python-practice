def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

if __name__ == "__main__":
    # Ask the user to input the temperature in Fahrenheit
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    
    # Convert the temperature to Celsius
    celsius = fahrenheit_to_celsius(fahrenheit)
    
    # Display the result
    print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")

