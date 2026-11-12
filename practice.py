for s in ["88","88.0","88分"," 88 "]:
    try:
        print(int(s))
    except ValueError:
        print("数值转换失败")
