sum_of_the_squares = 0
sum = 0

for i in range(1, 101):
    sum_of_the_squares += i**2
    sum += i

square_of_the_sum = sum**2
result = square_of_the_sum - sum_of_the_squares
        
print(f"Difference between the 'sum of the squares' and 'the square of the sum': {result}")