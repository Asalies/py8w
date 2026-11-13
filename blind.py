from pathlib import Path

SRC = Path("scores.txt")

def safe_load(path):
    rows = []
    with open(path,encoding="utf-8") as f:
        for lineno, line in enumerate(f,1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts)!=2:
                print(f"第{lineno}行格式不对，跳过：{line!r}")
                continue
            name, raw = parts
            try:
                score = int(raw)
            except ValueError:
                print(f"第{lineno}行分数不是整数，跳过：{line!r}")
                continue
            rows.append((name.strip(),score))
    return rows


if __name__ == "__main__":
    rows = safe_load(SRC)
    print(f"共读取到{len(rows)}条有效数据")
    for name, score in rows:
        print(f"{name}: {score}")
