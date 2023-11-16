# CTI-110
# P4HW2 - Salary Calculator
#Karli Monteith
#11/16/2023

#store totals
overtime_total = 0
regular_total = 0
gross_total = 0
num_employees = 0

#Loop to continuously ask for employee information
while True:
    #Ask for employee name
    employee_name = input("Enter employee name (or 'Done' to terminate program): ")

    #Check if user wants to terminate program
    if employee_name.lower() == "done":
        break

    #Ask for pay rate and hours worked
    pay_rate = float(input("Enter pay rate: "))
    hours_worked = float(input("Enter hours worked: "))

    #Calculate regular pay and overtime pay
    if hours_worked > 40:
        regular = 40 * pay_rate
        overtime = (hours_worked - 40) * (1.5 * pay_rate)
    else:
        regular = hours_worked * pay_rate
        overtime = 0

    #Calculate gross pay
    gross = regular + overtime

    #Update totals
    overtime_total += overtime
    regular_total += regular
    gross_total += gross
    num_employees += 1

#Display results
print("\nOvertime total: $", overtime_total)
print("Regular pay total: $", regular_total)
print("Gross pay total: $", gross_total)
print("Number of employees entered: ", num_employees)