import csv
import json
from pathlib import Path

CWD=Path(__file__).parent
SRC=CWD/"scores.txt"
DST=CWD/"tmp_test/scores.json"
def text_to_json(src=SRC, dst=DST):
    rows=[]
    with open(src,encoding="utf-8",newline="") as f:
        for lineno,line in enumerate(f,1):
            line = line.strip()
            if not line:
                continue
            # 门 3：这个值能变成我要的类型吗
            line=line.split(",")
            try:
                score = int(line[1].strip())

            except ValueError:
                print(f"第{lineno}行分数不是整数，跳过：{line!r}")
                continue
            rows.append({"姓名":line[0].strip(),"分数":score})
    DST.parent.mkdir(parents=True, exist_ok=True)
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
    if num:
        print(f"共{num}条有效数据！")
        total=sum(p['分数'] for p in data)
        print(f"总分：{total}  ",end="")
        print(f"平均分：{total/num}")
        for p in data:
            print(f"    {p['姓名']}: {p['分数']}")
    else:
        print("没有有效数据")
        raise SystemExit(1)
