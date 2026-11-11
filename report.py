from pathlib import Path

SRC = Path("scores.txt")
DST = Path("report.txt")

def load(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")          # 改这里
            if len(parts) != 2:
                print(f"第 {lineno} 行格式不对，跳过: {line!r}")
                continue
            name, score = parts
            rows.append((name, int(score)))
    return rows

def summarize(rows):
    if not rows:                          # 加保护
        return 0, 0.0, "", 0
    total = 0
    best_name, best_score = "", -1
    for name, score in rows:
        total += score
        if score > best_score:
            best_name, best_score = name, score
    return total, total / len(rows), best_name, best_score

if __name__ == "__main__":
    rows = load(SRC)
    total, avg, best_name, best_score = summarize(rows)
    lines = [
        f"人数: {len(rows)}",
        f"总分: {total}",
        f"平均分: {avg:.2f}",              # 去掉冒号后的空格
        f"最高分: {best_name} {best_score}",
    ]
    with open(DST, "w", encoding="utf-8") as f:
        for s in lines:
            f.write(s + "\n")
    for s in lines:
        print(s)
