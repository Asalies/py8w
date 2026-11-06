i = 1
j = 1
for i in range(1,10):
    for j in range(1,i+1):
        cell = f"{j}*{i}={i*j}"
        print(f"{cell:<8}",end="")
    print()
