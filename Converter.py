#Hello function

name= input("Hi, whats your name? ")

print("Hello ", name)

print("What are you looking to convert today?")

#Miles <-> Kilometers Conversion Function

def miles_to_km(miles):
    return miles * 1.609344

def km_to_miles(kilometers):
    return kilometers / 1.609344

#Fahrenheit <-> Celsius Conversion Function

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Light Years <-> Parsecs Conversion

def lightyrs_to_parsecs(lightyrs):
    return lightyrs * 0.3066014

def parsecs_to_lightyrs(parsecs):
    return parsecs / 0.3066014

while True:
    
    print("""        1. Miles to Kilometers | 2. Kilometers to Miles
          3. Farenheit to Celsius | 4. Celsius to Farenheit
          5. Lights Years to Parsecs | 6. Parsecs to Light Years 
          """)

    choice = input("Your Selection: ")

    if choice in ("1", "2", "3", "4", "5", "6"):
        try:
            num1 = float(input("Now what number are we converting? "))
        except ValueError:
            print("Invalid Input, Enter a number. ")
            continue

        if choice == "1":
            print(num1, "-----> km =", miles_to_km(num1), "km")
    
        elif choice == "2":
            print(num1, "----->", km_to_miles(num1), "m")
    
        elif choice == "3":
            print(num1, "----->", fahrenheit_to_celsius(num1), "C")

        elif choice == "4":
            print(num1, "----->", celsius_to_fahrenheit(num1), "F")

        elif choice == "5":
            print(num1, "----->", lightyrs_to_parsecs(num1), "parsecs")

        elif choice == "6":
            print(num1, "----->", parsecs_to_lightyrs(num1), "lightyrs")
        
    else:
        print("Invalid Selection. Please choose an option listed. ")
        continue


    another = input("How about another (Yes/No)? ")

    if another != "Yes":
        print("Sad to see you go!")
        break

    else:
        print("Great, let's go again!")