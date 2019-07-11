print('This is a program that reads two intergers and performs addition, subtraction, multiplication and dividsion on them.')
#request for user data
num_A = float(input('Enter a number: '))
num_B = float(input('Enter another number: '))

total_sum = float(num_A + num_B)
total_substraction = float(num_A - num_B)
total_multiplication = float(num_A * num_B)
total_division = float(num_A / num_B)

print(f'Sum: {total_sum}, subtraction: {total_substraction}, multiplication: {total_multiplication}, and division: {total_division} of the {num_A} and {num_B}.')
