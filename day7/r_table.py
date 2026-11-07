i=0
j=0
for i in range(1,10):
    for j in range(1,i+1):
        cell = f"{j}*{i}={j*i}"
        print(f"{cell:<7}",end="")
    print()
