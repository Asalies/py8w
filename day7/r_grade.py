score = float(input("请输入成绩："))

if score<0 or score>100:
    level = "输入无效，不与评级"
elif score >= 90:
    level = "A"
elif score >= 80:
    level = "B"
elif score >= 70:
    level = "C"
elif score >= 60:
    level = "D"
else:
    level = "F"
print(f"你的成绩评级：{level}")
