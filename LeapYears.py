#Hello Function

name=input("Hello, whats your name? ")

print(name)

print('''           A typical year on Earth is a 365 day period, in which we use to
      determine one full orbit around our big yellow sun. However, as most
      of us know, this 365 day period is not truthfuly exact, taking roughly
      a more honest 365.25 days. As it would be quite confusing to have
      a quarter of a day every year, we've decided to mark every four years as 
      a leap year, and within those years, adding the day of February 29th. How 
      do we determine what year is a leap year, every 4 years sounds simple until 
      we realize there's other factors at play. Is it divisible by 4 yet also 
      100, is it divisible by 100, but also divisible by 400. Lets
      simplify that process now. 
      ''')


#Function for determining leap year

while True:


    year= int(input("What year is on your mind? (Future, Past or Present!) "))

    if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
        print("This is in fact a leap year")
    else:
        print("This is in fact NOT a leap year")
    
    nextyear= input("Another year on your mind? ")

    if nextyear == "No":
        print("No problem, thank you for your time!")
        break
    elif nextyear == "Yes":
        continue
    else:
        print("Invalid Input")