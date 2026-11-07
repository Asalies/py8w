from random import randint

pwd = randint(1,100)
i=0
while i<6:
    i+=1
    num = int(input("请输入你猜测的数字："))
    if pwd == num:
        print(f"恭喜你仅用{i}次就猜中了")
        break
    elif pwd > num:
        print("偏小")
    else:
        print("偏大")
    if i==6:
        print(f"{pwd}")
