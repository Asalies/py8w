from pathlib import Path

print("cwd      =", Path.cwd())

print("本文件      =",Path(__file__))
print("脚本目录     =",Path(__file__).parent)

base = Path(__file__).parent
p = base/"scores.txt"
print("拼出来      =",p)
print("resolve    =",p.resolve())
print("存在吗      =",p.exists())

q = Path("data/2026/scores.txt")
print("name     =",q.name)
print("stem     =",q.stem)
print("suffix   =",q.suffix)
print("parent   =",q.parent)
