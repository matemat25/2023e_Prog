import random


# ismétlődő számok hányszor és hol szerepelnek?

numbers = []
repeated_numbers = []
for i in range(25):
    n = random.randint(1, 50)
    numbers.append(n)
print(numbers)

for i in range(len(numbers)):
    if numbers[i] in numbers[i+1:] and numbers[i] not in repeated_numbers:
        repeated_numbers.append(numbers[i])

for number in repeated_numbers:
    count = 0
    positions = []
    for i in range(len(numbers)):
        if numbers[i] == number:
            count += 1
            positions.append(i)
    print("A(z)",number, "szám", count, "alkalommal fordul elő a következő helyeken:", positions)