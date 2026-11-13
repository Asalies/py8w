import json

for s in ["88","88.0","88分"," 88 "]:
    try:
        print(int(s))
    except ValueError:
        print("数值转换失败")

def test():
    print(json.loads('{"n": 1}')["n"] + 1)
    print(json.loads('{"n": "1"}')["n"] + 1)

if __name__ == "__main__":
    test()
