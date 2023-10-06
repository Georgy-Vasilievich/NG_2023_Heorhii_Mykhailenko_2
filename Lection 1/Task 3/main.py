"""Convert Celsius to Farenheit and vice versa"""

conversion_type = int(input("""Enter 1 to convert Celsius to Farenheit,
2 to convert Farenheit to Celsius: """))
if conversion_type == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"Farenheit: {celsius * 9/5 + 32}")
elif conversion_type == 2:
    farenheit = float(input("Enter temperature in Farenheit: "))
    print(f"Celsius: {5/9 * (farenheit - 32)}")
