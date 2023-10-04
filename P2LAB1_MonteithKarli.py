#enter the mileage variable 
mileage = float(input())
#find the cost per mileage
cost = float(input())
#multiply the mileage times cost
cost_20 = 20 / mileage * cost
cost_75 = 75 / mileage * cost
cost_500 = 500 / mileage *cost
#find the end cost
print(f'{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}')