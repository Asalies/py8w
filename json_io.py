import json
from pathlib import Path

SRC = Path("scores.txt")
DST = Path("scores.json")

def txt_to_json(src=SRC, dst=DST):
    rows = []
    with open(src,encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, raw = line.split(",")
            rows.append({"姓名": name.strip(), "分数": int(raw)})
    with open(dst,"w",encoding="utf-8") as f:
        json.dump(rows,f,ensure_ascii=False,indent=2)
    return dst

def read_json(path=DST):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    txt_to_json()
    data = read_json()
    print(f"共{len(data)}人")
    total = sum(p["分数"] for p in data)
    print(f"总分 {total}, 平均 {total / len(data):.2f}")
    for p in data:
        print(f"  {p['姓名']}: {p['分数']}")
