import json
from pathlib import Path

import requests

CWD = Path(__file__).parent
DST = CWD / "tmp_test" / "remote.json"
URL = "https://jsonplaceholder.typicode.com/todos/1"

def fetch(url=URL):
    r = requests.get(url,timeout=5)
    r.raise_for_status() #r.raise_for_status()把4xx/5xx变为异常
    return r.json()

def save(data,dst=DST):
    dst.parent.mkdir(parents=True,exist_ok=True)
    with open(dst,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
    return dst

def main():
    try:
        data = fetch()
    except requests.exceptions.RequestException as e:
        print(f"请求失败：{e}")
        raise SystemExit(1)
    print(data)
    save(data)

if __name__ == "__main__":
    main()
    data = fetch()
    print(type(data))
    print(type(data["id"]))
    print(data["id"] + 1)
