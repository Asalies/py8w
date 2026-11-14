import csv
from pathlib import Path

SRC = Path(__file__).parent/"scores.txt"

def safe_load(path):
    rows = []
    with open(path,encoding="utf-8",newline="") as f:
        reader = csv.reader(f)
        for lineno,row in enumerate(reader,1):
            if not row or all(not c.strip() for c in row):
                continue
            if len(row)!=2:
                print(f"第{lineno}行格式不对，跳过：{row!r}")
                continue
            name,raw = row[0].strip(),row[1].strip()
            try:
                score = int(raw)
            except ValueError:
                print(f"第{lineno}行分数不是整数，跳过：{row!r}")
                continue
            rows.append((name,score))
    return rows

if __name__ == "__main__":
    rows = safe_load(SRC)
    print(f"共{len(rows)}条有效数据")
    for name,score in rows:
        print(f"    name: {name},score: {score}")


























# import csv
# from pathlib import Path
#
# SRC = Path("scores.txt")
#
# def safe_load(path):
#     rows = []
#     with open(path,encoding="utf-8",newline="") as f:
#         reader = csv.reader(f)
#         for lineno, row in enumerate(reader, 1):
#             if not row or all(not c.strip() for c in row):
#                 continue
#             if len(row) != 2:
#                 print(f"第{lineno}行格式不对，跳过：{row!r}")
#                 continue
#             name, raw = row[0].strip(),row[1].strip()
#             try:
#                 score = int(raw)
#             except ValueError:
#                 print(f"第{lineno}行分数不是整数，跳过：{row!r}")
#                 continue
#             rows.append((name,score))
#     return rows
#
# if __name__ == "__main__":
#     rows = safe_load(SRC)
#     print(f"读到{len(rows)}条有效数据")
#     for name, score in rows:
#         print(f"    {name}: {score}")
