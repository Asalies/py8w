sum = 0
tries = 0
for tries in range(1,101):
    sum +=tries
print(sum)

sum = 0
tires = 0
for tries in range(1,101):
    if (tries%2) == 0:
        sum +=tries
print(sum)

sum = 0
tires = 0
for tries in range(1,101):
    if (tries%3) == 0:
        sum +=tries
print(sum)

sum = 0
tires = 0
for tries in range(1,101):
    if (tries%3) == 0 and (tries%5) == 0:
        sum +=tries
print(sum)
