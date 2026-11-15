import math

raw =input("请输入成绩：")

try:
    score = float(raw)
except ValueError:
    print(f"输入格式不对，{raw!r}不是数值")
    raise SystemExit(1)
if math.isnan(score) or score<0 or score>100:
    print(f"{score!r}不在范围内")
    raise SystemExit(1)
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
