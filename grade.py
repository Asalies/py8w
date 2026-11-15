score = float(input("请输入成绩："))
if score < 0 or score > 100:
    level = "输入无效，不给等级"
elif score >= 90:
    level = "A，及格"
elif score >= 80:
    level = "B，及格"
elif score >= 70:
    level = "C，及格"
elif score >= 60:
    level = "D，及格"
else:
    level = "F，不及格"
print(f"{level}")
