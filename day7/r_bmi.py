hight = float(input("请输入身高（米）："))
weight = float(input("请输入体重（kg）："))

result = weight/(hight**2)

if result < 18.5:
    label = "偏瘦"
elif result < 24:
    label = "正常"
elif result < 28:
    label = "偏胖"
else:
    label = "肥胖"


print(f"你的BMI：{result:.2f}，你的身材{label}")
