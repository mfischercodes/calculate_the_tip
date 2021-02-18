''' Display tip percentages based on your totaal bill amount '''

def total_bill():
    bill = float(input("\nWhat's your total bill today? "))

    def tip():
        print( f"\n10% {round(bill*0.10,2)} \n15% {round(bill*0.15,2)} \n20% {round(bill*0.20,2)}\n")
        tip_amount = (bill * (round(float(input("How much would you like to tip? ")),2)) / 100)
        return tip_amount

    def total():
        print(f"You're total comes to ${round(bill + tip_amount,2)}")
    
    tip_amount = tip()
    total()

total_bill()


    


