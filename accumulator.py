total = 0
for i in range(1,101):
    total +=i
print(total)

total = 0
for i in range(1,101):
    if (i%2) == 0:
        total +=i
print(total)

total = 0
for i in range(1,101):
    if (i%3) == 0:
        total +=i
print(total)

total = 0
for i in range(1,101):
    if (i%3) == 0 and (i%5) == 0:
        total +=i
print(total)
