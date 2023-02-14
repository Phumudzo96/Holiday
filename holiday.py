def hotal_cost():                           # create a function thay will store my code
    stay_price = 500.00                     # creat a varible with the price of the hotel stay
    stay = int(input("How many nights will you be staying here: ")) # Ask user about the number of nights
    total = stay_price * stay               # calculate the number of night with the price of the hotel stay 
    print(f"The amount for your stay is R{total}") # print out the total
    


def plane_cost():                           
    JHB = 1000.00                            # create variables with set flight prices
    CPT = 1500.00
    DBN = 1250.00
    PMB = 950.00
    plane = input('''Where are you flying to?  
    JHB = 1000.00
    CPT = 1500.00
    DBN = 1250.00
    PMB = 950.00: ''').upper()               # ask the user where they are flying to

    if plane == "JHB":                       # if a user select of the four places, the selected prices should be displayed
            ftotal = JHB
            print(f"The flight amount is R{JHB}")
    elif plane == "CPT":
            ftotal = CPT
            print(f"The flight amount is R{CPT}")
    elif plane == "DBN":
            ftotal = DBN
            print(f"The flight amount is R{DBN}")
    elif plane == "PMB":
            ftotal = PMB
            print(f"The flight amount is R{PMB}")
    else:
        print("Invalid selection")



def car_rental():
    car = 250.00                         # create a variable with the set price of renting a car 
    rent = int(input("For how many days wiil you rent the car: ")) # ask for how many days will they be renting the car
    total = car * rent                   # calculate the price of renting the car with how many days they will be renting the car
    print(f"The amount to rent the car is R{total}") # print out the total


def holiday_cost():
    stay_price = 500.00
    stay = int(input("How many nights will you be staying here: "))
    total = stay_price * stay
    
    JHB = 1000.00
    CPT = 1500.00
    DBN = 1250.00
    PMB = 950.00
    plane = input('''Where are you flying to? 
    JHB = 1000.00
    CPT = 1500.00
    DBN = 1250.00
    PMB = 950.00: ''').upper()

    if plane == "JHB":
            ftotal = JHB
            print(f"The flight amount is R{JHB}")
    elif plane == "CPT":
            ftotal = CPT
            print(f"The flight amount is R{CPT}")
    elif plane == "DBN":
            ftotal = DBN
            print(f"The flight amount is R{DBN}")
    elif plane == "PMB":
            ftotal = PMB
            print(f"The flight amount is R{PMB}")
    else:
        print("Invalid selection")

 
    car = 250.00
    rent = int(input("For how many days wiil you rent the car: "))
    total1 = car * rent
    
    total_cost = ftotal + total + total1  # calucalate the total of the hotel stay,flight and car rent
    print(f"The cost for the whole trip is R{total_cost}") # print the cost of the whole trip
    

holiday_cost()


