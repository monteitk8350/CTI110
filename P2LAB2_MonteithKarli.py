#numbers given for problem
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

#calculate and average
your_value = num1 * num2 * num3 * num4 
average = (num1 + num2 + num3 + num4 )/4
#output as integers
print(f'{your_value:.0f}') 

print(f'{average:.0f}')


#output as floating point numbers
print(f'{your_value:.3f}') 

#output as floating average
print(f'{average:.3f}')