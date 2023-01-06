# There is a solution to this problem in 4 minutes and 30 seconds. 
# In the example in the example, the result is available instantly.

i = 0

while True:
    i += 1
    flag = True
    for j in range(1, 21):
        if (i % j == 0):
            continue
        else:
            flag = False
            break
    if (flag == True):
        break

print(f"Smallest number divisible by numbers from 1 to 20 without a remainder: {i}")