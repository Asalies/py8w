import csv
import json
from pathlib import Path

CWD=Path(__file__).parent
SRC=CWD/"scores.txt"
DST=CWD/"tmp_test/scores.json"
def text_to_json(src=SRC, dst=DST):
    rows=[]
    with open(src,encoding="utf-8",newline="") as f:
        reader=csv.reader(f)
        for line in reader:
            if not line:
                continue
            name,raw=line[0].strip(),line[1].strip()
            rows.append({"姓名":name.strip(),"分数":int(raw)})
    with open(dst,"w",encoding="utf-8") as f:
        json.dump(rows,f,ensure_ascii=False,indent=2)
    return dst

def safe_json(dst=DST):
    with open(dst,encoding="utf-8") as f:
        return json.load(f)

if __name__=="__main__":
    text_to_json()
    data=safe_json()
    num=len(data)
    print(f"共{num}条有效数据！")
    total=sum(p['分数'] for p in data)
    print(f"总分：{total}  ",end="")
    print(f"平均分：{total/num}")
    for p in data:
        print(f"    {p['姓名']}: {p['分数']}")
