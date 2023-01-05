# For the number 600851475143, this algorithm 
# is very slow but works correctly.

# In order for the program to be faster, 
# I need to learn other methods that I researched on the internet.

number = 13195 
list = []
flag = True
for i in range(2, number//2):
    if (number % i == 0):
        for j in range(2, i//2):
            if (i % j == 0):
                flag = False
                break
        if (flag == True):
            list.append(i)

print(list)