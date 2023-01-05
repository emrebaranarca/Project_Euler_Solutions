# Method 1
total = 0
for number in range(0, 1000):
    if (number % 3 == 0) or (number % 5 == 0):
        total += number

print(total)


# Method 2
list = []
for number in range(0, 1000):
    if (number % 3 == 0) or (number % 5 == 0):
        list.append(number)

total = sum(list)
print(total)