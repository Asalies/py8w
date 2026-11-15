height = float(input("请输入身高（米）："))
weight = float(input("请输入体重（KG）："))
bmi = weight / (height ** 2)
if bmi < 18.5:
    label = "偏瘦"
elif bmi < 24:
    label = "正常"
elif bmi < 28:
    label = "偏胖"
else:
    label = "肥胖"
print(f"BMI = {bmi:.2f}，属于{label}")
