s=7385
h,rem = divmod(s,3600)
m,sec = divmod(rem, 60)
print (f"{h}:{m:02d}:{sec:02d}")
print(f"{s} 秒 = {h} 小时 {m} 分 {sec} 秒")
