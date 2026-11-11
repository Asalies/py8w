import random
num = random.randint(1,100)
i = 0
while 1:
    i +=1
    num2 = int(input("请输入你的猜测："))
    if num2 > num:
        print("太大了")
    elif num2 < num:
        print("太小了")
    else:
        print(f"猜对了，{i}次就猜对了")
        break
    #if i == 6:
    #    print(f"电脑选择的是{num}")
