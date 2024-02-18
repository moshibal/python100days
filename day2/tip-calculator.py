print("welcome to tip calculator")
total_bill=float(input("what was the total bill?"))
num_of_people=int(input("how many people to split the bill?"))
percent_tip=int(input("what percentage of tip would you like to give? 10, 12, or 15?"))
bill_per_person=(total_bill+(total_bill*(percent_tip/100)))/num_of_people
print(f"Each person should pay: $ {round(bill_per_person,1)}")