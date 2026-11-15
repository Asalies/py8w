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
        for lineno,row in enumerate(reader,1):
            if not row or all(not c.strip() for c in row):
                continue
            if len(row) != 2:
                print(f"第{lineno}行格式不对，跳过：{row!r}")
                continue

            # 门 3：这个值能变成我要的类型吗
            try:
                score = int(row[1].strip())
            except ValueError:
                print(f"第{lineno}行分数不是整数，跳过：{row!r}")
                continue
            rows.append({"姓名":row[0].strip(),"分数":score})
    with open(dst,"w",encoding="utf-8") as f:
        json.dump(rows,f,ensure_ascii=False,indent=2)
    return dst

def safe_json(dst=DST):
    with open(dst,encoding="utf-8") as f:
        return json.load(f)

if __name__=="__main__":
    DST.parent.mkdir(parents=True, exist_ok=True)
    text_to_json()
    data=safe_json()
    num=len(data)
    print(f"共{num}条有效数据！")
    total=sum(p['分数'] for p in data)
    print(f"总分：{total}  ",end="")
    print(f"平均分：{total/num}")
    for p in data:
        print(f"    {p['姓名']}: {p['分数']}")
