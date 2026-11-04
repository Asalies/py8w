grade = float(input("请输入成绩："))
if grade < 0 or grade > 100:
    level = "输入无效，不给等级"
elif grade >= 90:
    level = "A，及格"
elif grade >= 80:
    level = "B，及格"
elif grade >= 70:
    level = "C，及格"
elif grade >= 60:
    level = "D，及格"
else:
    level = "F，不及格"
print(f"{level}")
