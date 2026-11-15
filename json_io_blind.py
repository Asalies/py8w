import json
from pathlib import Path

CWD = Path(__file__).parent
SRC = CWD/"scores.txt"
DST = CWD/"tmp_test"/"scores.json"

def txt_to_json(src=SRC,dst=DST):
    rows=[]
    with open(src,encoding="utf-8") as f:
        for lineno,line in enumerate(f,1):
            line = line.strip().split(",")
            if not line:
                continue
            if len(line)!=2:
                print(f"第{lineno}行格式不对，跳过：{line!r}")
                continue
            name,raw=line[0].strip(),line[1].strip()
            try:
                score = int(raw)
            except ValueError:
                print(f"第{lineno}行分数不是整数，跳过：{line!r}")
                continue
            rows.append((name.strip(),score))
    dst.parent.mkdir(parents=True,exist_ok=True)
    with open(dst,"w",encoding="utf-8") as f:
        json.dump(rows,f,ensure_ascii=False,indent=2)
    return dst

def safe_json(dst=DST):
    with open(dst,encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    txt_to_json()
    data = safe_json()
    num = len(data)
    if num == 0:
        print("无有效数据，程序已结束！")
        raise SystemExit(1)
    print(f"共{num}条有效数据")
    total=sum(c[1] for c in data)
    print(f"总分：{total}, 平均分：{total/num}")
    for name,score in data:
        print(f"    {name}: {score}")
