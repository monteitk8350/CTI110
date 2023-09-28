#travel expenses for a trip
#09/28/2023
#CTI-110 P1HW2 - Travel Expense
#Karli Monteith

#page title for what is going to be done in this program
print("This program calculates and displays travel expenses")
#ask user to enter their budget
budget = float (input("Enter Budget: "))
#ask user to enter their travel destination
trav_des = (input("Enter your travel destination: "))
#ask user for the amoun t they will spend on gas
gas = float (input("How much do you think you will spend on gas? "))
#ask uder for the amount they will spend on accomodations
lodge = float (input("Approximately, how much will you need for accomodations/hotel? "))
#ask user for amount they will spend on food
food = float (input("Last, how much do you need for food? " ))

print("------------Travel Expenses------------")
#summarize information you have recievd
print(f'Location: {trav_des}')
print(f"Initial Budget: {budget} ")

print(f'Fuel: {gas} ')
print(f'Accomodation: {lodge} ')
print(f'Food: {food} ')
rem_bal = (budget) - (gas) - (lodge) - (food)
#subtract expenses from initial budget
print(f'Remaining Balance: {rem_bal}')