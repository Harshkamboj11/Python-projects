temp_value = float(input("enter the temperatue: "))
conversion = input("conversion type(C to F, C to K, F to C, F to K, K to C, K to F): ").lower()

if conversion == 'c to f':
    formula = 9/5*temp_value+32
    print(f"{temp_value} to fahrenheit is {formula}")
elif conversion == 'c to k':
    formula2 = temp_value + 273.15
    print(f"{temp_value} to kelvin is {formula2}")
elif conversion == 'f to c':
    formula3 = 5/9 * (temp_value-32)
    print(f"{temp_value} to celcius is {formula3}")
elif conversion == 'f to k':
    formula4 = 5/9 * (temp_value-32) + 273.15
    print(f"{temp_value} to kelvin is {formula4}")
elif conversion == 'k to c':
    formula5 = temp_value-273.15
    print(f"{temp_value} to celcius is {formula5}")
elif conversion == 'k to f':
    formula6 = 9/5 * (temp_value-273.15)+32
    print(f"{temp_value} to fahrenheit is {formula6}")
else:
    print("invalid conversion type....")
