def c_to_f(c):
    return c * 9 / 5 + 32

def grade(score):
    if score < 0 or score > 100:
        return "输入无效"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

def row(n, end=9):
    for j in range(1, end + 1):
        cell = f"{j}*{n}={j*n}"
        print(f"{cell:<8}", end="")
    print()

def main():
    print(f"100C = {c_to_f(100)}F")
    print(f"90分 -> {grade(90)}")
    print(f"105分 -> {grade(105)}")
    row(3)

main()
