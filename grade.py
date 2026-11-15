import math

raw = input("请输入成绩：")
try:
    score = float(raw)
except ValueError:
    print(f"输入格式不对，{raw!r}不是数字")
    raise SystemExit(1)

if math.isnan(score) or score < 0 or score > 100:
    print(f"{score!r}不在范围内")
    raise SystemExit(1)
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
