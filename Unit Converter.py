# this is a simple unit converter that converts between different units of measurement
print("1. km to miles")
print("2. kg to pounds")
print("3. cm to inches")
print("4. liters to gallons")
print("5. Celsius to Fahrenheit")
print("6. acre to square meters")
print("7. feet to meters")
print("8. gunta to square meters")

choices = str(input("choice the options : "))
if choices == "1":
   km = float(input("Enter the value in kilometers: "))
   miles = km * 0.621371
   print(f"{km} kilometers is equal to {miles} miles.")

elif choices == "2": 
    kg = float(input("Enter the value in kilograms: "))
    pounds = kg * 2.20462
    print(f"{kg} kilograms is equal to {pounds} pounds.")

elif choices == "3":
    # cm to inches
    cm = float(input("Enter the value in centimeters: "))   
    inches = cm * 0.393701
    print(f"{cm} centimeters is equal to {inches} inches.")

elif choices == "4":
    # liters to gallons
    liters = float(input("Enter the value in liters: "))
    gallons = liters * 0.264172
    print(f"{liters} liters is equal to {gallons} gallons.")

elif choices == "5":
    # Celsius to Fahrenheit
    celsius = float(input("Enter the value in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

elif choices == "6":
    # acre to square meters
    acres = float(input("Enter the value in acres: "))
    square_meters = acres * 4046.86
    print(f"{acres} acres is equal to {square_meters} square meters.")

elif choices == "7":
    # feet to meters
    feet = float(input("Enter the value in feet: "))    
    meters = feet * 0.3048
    print(f"{feet} feet is equal to {meters} meters.")

elif choices == "8":
    # gunta to square meters
    gunta = float(input("Enter the value in gunta: "))
    square_meters_gunta = gunta * 101.1714
    print(f"{gunta} gunta is equal to {square_meters_gunta} square meters.")

else:
    print("Invalid choice. Please select a valid option from the menu.")