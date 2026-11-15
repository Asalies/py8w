# 2026/11/4

### 做了什么
name.py：把 "  li   ming  " 去掉两端空格、切成两段，取首字母大写加 "."，输出 L.M.，再查看名字和分段长度。
lab_types.py：七条动手检测——type()、/ 与 // 与 %、** 幂、round()、len()/upper()/split()、字符串 * 和 +、整数加浮点。
bmi.py：输入身高体重算 BMI，用 if/elif 分偏瘦/正常/偏胖/肥胖。
grade.py：输入成绩，先挡 0–100 之外，再按 90/80/70/60 分 A–F。

### 学到了什么
input() 拿到的永远是 str，要算数必须先 float() 或 int() 转换——这是今天最大的收获。
f-string 里 {bmi:.2f} 是两位小数，格式说明必须写在花括号里面。
/ 得到浮点，// 是整除，% 是取余；type() 看类型，round(x, 2) 保留两位。
.strip() 去两端空白，.split() 按空白切成列表，可以接着取 p[0]。
if/elif/else 从上往下判断，第一个成立就停，后面的不再看。

### 卡在哪
一开始直接拿 input() 的结果去做除法，str 不能参与算术，必须先转换。
逗号版 print(bmi, label) 里写 .2f 完全无效，点号两位小数只认 f-string 的花括号。

### 明天从哪继续
11/5：循环。用 while 和 for 写猜数字游戏，练计数器和提前跳出。

# 2026/11/5

### 做了什么
guess.py：电脑在 1–100 里随机取一个数，最多猜 6 次，每次告诉"太大了/太小了"，猜对报出用了第几次，6 次用完打印答案。
lab_loop.py：range() 三种写法、for 累加求和、while 计数器。

### 学到了什么
while 循环的计数器要自己维护，Python 没有 i++，只能写 i += 1。
range(1, 6) 右端不含，只到 5；而 random.randint(1, 100) 两端都包含。差一个的坑这两种写法正好相反，要分开记。
break 提前跳出整个循环，"猜对了"之后不再继续问。

### 卡在哪
写 i++ 直接报错——Python 没有自增运算符，这个习惯得从别的语言里改掉。
range 的右端不含容易算错一次，写完要盯着数字念一遍。

### 明天从哪继续
11/6：用循环打印九九乘法表，练 end="" 不换行和定宽对齐。

# 2026/11/6

### 做了什么
table.py：用两层 for 打印九九乘法表，第 i 行只打到 i*j，每格定宽 8 个字符，行末换行。

### 学到了什么
print(..., end="") 让这一行不换行，一整行打完后用空的 print() 补一个换行。
定宽用 f"{cell:<8}"：< 左对齐，8 是总宽度，补空格到 8 位，表格才对得齐。
内层 range(1, i+1) 让第 i 行正好打 i 格，自然形成三角。

### 卡在哪
宽度只能作用于整个值，不能只给后面某一小段定宽；必须先把一格拼成完整字符串 cell，再对 cell 定宽，否则列还是会歪。

### 明天从哪继续
11/7：不看书，把前四天的程序盲写一遍，检验哪些是真会、哪些只是看着眼熟。

# 2026/11/7

### 做了什么
day7/ 目录里盲写重写五个程序：r_bmi.py、r_grade.py、r_guess.py、r_hello.py、r_table.py，全程不翻之前的代码。

### 学到了什么
盲写和看着写是两件事——能默写出来才算会。
重写 r_bmi.py 时把输出改成 {result:.2f}，"你的BMI：22.86"比第一次干净多了。

### 卡在哪
整体还算顺利，没卡住。但变量名拼写不稳：hight 应该是 height，hight_m 也一样，跑得通但读起来别扭，以后拼错的变量名最容易在回头改代码时找不到。

### 明天从哪继续
11/8：复盘 + 虚拟环境，搞清楚 .venv 到底隔离了什么。

# 2026/11/8 复盘

### 做了什么
确认 .venv 隔离有效：删掉能重建 = 只依赖 requirements.txt。

### 学到了什么
不建 venv 的话，pip install 全局只有一份 site-packages，多项目会版本冲突，
且装坏系统 Python 时没有"删掉重建"这个退路。venv 的成本是 1 分钟，不建的成本是几小时。

### 卡在哪
暂时没有——但还没试过"删掉 .venv 再重建"这条命令，只是推理。

### 明天从哪继续
11/9：函数。把 BMI、成绩分档这些重复逻辑收进 def 里，用 return 交结果。

# 2026/11/9

### 做了什么
func.py：c_to_f 摄氏转华氏、grade 分数分档（带 0–100 边界保护）、row 打印乘法表某一行、main() 串起来依次调用。

### 学到了什么
def 定义函数，参数写在括号里，return 把结果交回调用处。
没有 return 的函数返回 None，拿它去格式化就会出事。
默认参数 end=9：不传就用 9，传了就按传的来。
参数顺序有硬规则：有默认值的必须排在没默认值的后面。

### 卡在哪
def f(a=1, b): 报 SyntaxError: parameter without a default follows parameter with a default——默认参数不能排在无默认参数前面。
函数体忘了缩进报 IndentationError。
函数忘了写 return，再拿回来做 :.2f 格式化，报 TypeError: unsupported format string passed to NoneType.__format__——没想到是"没返回值"引起的。
return 后面的代码静默不执行，不报错也不提示，最容易看漏。

### 明天从哪继续
11/10：模块。把这些函数挪进 tools.py，用 import 在别的文件里调用。

# 2026/11/10

### 做了什么
tools.py：把 c_to_f、grade、row 三个函数放进去。
day10.py：先 import tools 用 tools.c_to_f(0) 调用，再 from tools import c_to_f, grade 直接调用，最后打印 tools.__name__ 观察模块名。

### 学到了什么
import 会把被导入的文件整个执行一遍——所以 tools.py 里的 print 会跟着跑。
if __name__ == "__main__": 只有本文件直接运行时才执行块内代码，被 import 时不执行。这是防止"一 import 就打印一堆"的标准写法。
from m import f 只拿指定的名字，调用时不用写前缀。
同一进程里第二次 import 不会重新读文件，模块已经缓存了。

### 卡在哪
自己写了个 random.py 做实验，结果 import random 拿到的是自己写的 randint，真打出 42——文件名和标准库同名，会把自己的文件顶上去。禁区：random.py / math.py / time.py / json.py / os.py / sys.py / string.py / email.py / types.py。
import toolz 报 ModuleNotFoundError（模块不存在），from tools import c2f 报 ImportError（模块在、名字不在），两种错要分得清。

### 明天从哪继续
11/11：文件读写。把分数存进 scores.txt，用 with open + enumerate 逐行读出来统计。

# 2026/11/11

### 做了什么
写了 scores.txt 四行数据（张三,88 李四,95 王五,72 赵六,60），report.py 用 with open + enumerate(f,1) 逐行读，算出人数、总分、平均分、最高分，写进 report.txt。

### 学到了什么
enumerate(f, 1) 一次同时给行号和内容，空行也照样占行号。
strip() 必须最先做，每行结尾带 \n，不 strip 的话名字里会留着换行。
坏行只报 ValueError 分不出原因，必须打印 repr(line) 才看得见是全角逗号、空格还是 Tab。

### 卡在哪
把报表写进了数据文件：DST 写成 scores.txt，用 "w" 一打开就把四行原始数据清空了。
之后重跑只报 ZeroDivisionError: division by zero——不是逻辑写错，是数据先没了。
"w" 是清空再写，不是追加，这个必须先想清楚再落笔。

### 明天从哪继续
文件读写基本走通。明天学 try/except：读到"分数不是整数"这种坏行时，不中断、报出行号、跳过继续读下一行。

# 2026/11/12

### 做了什么
写 safe_load.py：读分数文件，坏行跳过并报行号，好行照常返回。
加练 practice.py：用 try/except 包住 int() 的转换，让四个值全部跑完。

### 学到了什么
int() 只认整数字面量。' 88 ' 和 '88\n' 能过（两端空白自动吸掉），但 '88.0' 和 '88分' 都报 ValueError。
要小数得用 float()；可 int(float('88.9')) 会悄悄变成 88，所以坏行应该报出来让人看，不该替它猜。
try 只包 int(raw) 这一句，报错才知道是哪一步出的问题。
except ValueError as e 能拿到原始错误信息，比只写一句"转换失败"有用得多。

### 卡在哪
我原以为 '88分' 和 ' 88 ' 会崩、'88.0' 能过，实际正好反了。
更关键的是：未捕获的 ValueError 会在第二行就终止整个程序，后面几行根本没执行，
所以我之前从输出里"推断"出 ' 88 ' 也会崩，其实那一行从来没跑过。

### 明天从哪继续
11/13：JSON / csv 模块。今天 safe_load.py 手写的 split + 判断，用 csv 模块几行就能替掉。

# 2026/11/13

### 做了什么
safe_load_v2.py 用 csv 模块重写；json_io.py 完成 txt→json→读回

### 学到了什么
今天至少有三条：strip 要用 = 接住、手写 split 遇引号会错位、json 带类型

### 卡在哪
盲敲漏了 strip()，靠对照才发现。原因：不知道它为什么存在

### 明天从哪继续
11/14：`pathlib` 路径操作 + 搞清「当前工作目录」。今天写的 `SRC = Path("scores.txt")` 是相对路径，只在 `D:\Project\py8w` 里跑得通，换个目录运行就找不到文件。
遗留：`accumulator.py` 三处 `tires` 拼写错（应为 `tries`）；`bmi.py` / `grade.py` / `r_bmi.py` 的 `hight` 未改。

# 2026/11/14

### 做了什么
paths.py 摸清三个「在哪」；safe_load_v2.py 改用 __file__

### 学到了什么
相对路径的起点是 cwd 不是脚本、__file__ 是稳定锚点、Path.cwd() 会变、Path().parent取父目录

### 卡在哪
row取值时，下标从1开始了，看之前记录才发觉。

### 明天从哪继续
11/15：周日复盘，不学新内容。先把两次没落盘的东西补上——`.gitignore` 删掉 `tricky.csv` 那行后 `git add tricky.csv`；`safe_load_v2.py` 删首行空行、`import csv` 挪到 `from pathlib` 之后、`SRC` 改成 `Path(__file__).parent / "scores.txt"`、`print(f"  {name}: {score}")` 补回两个空格；然后在 `tmp_test/` 里跑 `python ..\safe_load_v2.py`，必须仍读到 4 条。
复盘重点：这周撞了五次「不报错的错」——`strip()` 没用 `=` 接住、手写 `split` 遇引号错位、`json` 的 `"1"` 是 `str`、`.gitignore` 静默拦掉手写数据、`p.suffix` 是 `".txt"` 不是 `"txt"`。
遗留：`accumulator.py` 三处 `tires`→`tries`；`bmi.py` / `r_bmi.py` 的 `hight`→`height`。

# 2026/11/15 
## 复盘（11/9–11/14）
### 这周做了什么
- 11/9  函数：def / return / 默认参数
- 11/10 模块：import / `__name__` / from import
- 11/11 文件读写：with / enumerate / writelines
- 11/12 异常：try/except 只包 int(raw)
- 11/13 csv/JSON：标准库替掉手写 split
- 11/14 pathlib：cwd 与脚本目录的区别
- 11/15 删除accumulator无关变量并修改变量名，增加grade的异常判断，修改bmi的变量名
- accumulator.py：sum→total（4处，原遮蔽内置 sum）、tires=0 三行删除（死代码，改名无效）
- bmi.py：hight_m→height（2处）、weight_h→weight（2处，注意不是 height）
- r_bmi.py：hight→height（2处），weight 本来就对
- grade.py：补 try/except ValueError + math.isnan，26 组输入全过

### 这周的六个「不报错的错」
1. `strip()` 不用 `=` 接住，`if l.strip()` 只判断不改 l
2. 手写 `split` 遇引号内逗号，列会错位但照样返回
3. `json` 的 `"1"` 是 str，`+ 1` 才报错
4. `.gitignore` 拦了手写测试数据，`git add` 静默跳过
5. `p.suffix` 是 `".txt"` 不是 `"txt"`
6. 两个 pip 不是冲突
where.exe pip 列出 2 条 = 按 PATH 顺序列出全部同名命令，不是报错。
venv 的 Activate.ps1 第 246-247 行：先用 _OLD_VIRTUAL_PATH 存原 PATH，
再把 .venv\Scripts 插到最前。deactivate 再还原。
裸写 pip 只执行第一条 → 顺序决定装到哪里。
venv 里其实有 3 个壳子：pip.exe / pip3.exe / pip3.11.exe。
真正的 pip 是 Lib\site-packages\pip\ 目录，壳子删了 python -m pip 照样用，
但 ensurepip 不会把它装回来（实测删 pip.exe 后 ensurepip --upgrade 无效果）。
结论：一个都别删，命令一律写 python -m pip。
（六条是同一个模式：跑得通，但结果错）

### 卡在哪
print 缩进补错成 `name:` 格式，在写循环读取时还是有点不太明白不知道该怎么写，想了一下是根据数据格式进行判断
try/except ValueError 只拦「字符串不能转数字」，拦不住 nan。
float('nan') 是成功转换，不抛异常；而 nan 的所有比较都返回 False，
于是绕过「无效输入」门一路滑进 else，输出「F，不及格」还不报错。
识别：math.isnan(x) 或 x != x。

## 加学
### 做了什么
- python -m pip 自证归属（sys.prefix 含 .venv、pip --version 路径含 .venv）
- install requests：1 个库带进 4 个依赖，freeze 0 行 → 5 行
- requirements.txt 入库（git check-ignore 确认未被忽略）
- day16.py：requests.get(timeout=5) → raise_for_status → json() → 落盘 ensure_ascii=False
- 主动删 tmp_test 重跑，验证 mkdir 在函数内

### 学到了什么
- pip 是独立程序，裸写 pip 有歧义；python -m pip 用「当前这个 python」的 pip
- 依赖：只要 requests，来 certifi / charset_normalizer / idna / urllib3
- 失败分两层：网络层（Timeout/ConnectionError，拿不到 status_code）vs HTTP 层（403/404，能拿到 status_code）
- raise_for_status() 把 HTTP 层失败变成异常；RequestException 是三者共同父类，一句兜住
- 403 ≠ 404：403 是「不给你」，404 是「没有」
- r.json() 里的数字还是 int，不用再转

### 卡在哪
执行时显示了r.json()但是有报错No such file or directory，发现是没写创建文件语句

### 验收通过 ≠ 参数生效
day16.py 落盘后看到结构正确，就以为 ensure_ascii=False 验证过了。
但 jsonplaceholder todo/1 全是英文，实测参数开与关输出逐字节相同。
ensure_ascii 只影响非 ASCII 字符的 \u 转义，数据里没有汉字，它就没有作用对象。
真正被验证的：indent=2、False→false、dict 保序。
教训：验收标准要保证「被验的东西的作用对象」真的出现在数据里。

### 明天从哪继续
- 编码坑：响应头没有 charset 时 requests 会猜编码
  （text/html 猜 ISO-8859-1，中文必乱码）；
  最阴的是 r.json() 在编码猜错时不报错，返回键名乱码的 dict，rc=0。
- 补完 Get-Content tmp_test\remote.json 的确认
### 补：ensure_ascii=False 双向验证完成
python -c ... 写入 {'备注':'中文'} 到 t.json（encoding='utf-8'）
Get-Content t.json -Encoding utf8 → {"备注": "中文"}，汉字保住。

- 参数只管非 ASCII 字符：True/省略 → \u5907\u6ce8；False → 备注。
  上次 todo/1 全英文，开关拨哪边都一样，所以什么也没验证。
  这次数据里有汉字，两个方向都看到了，才算验证完成。
- encoding='utf-8' 必须写在 open() 里。少了它 Windows 默认 cp936，
  文件变成 GBK 字节，和 UTF-8 字节完全不同：
  UTF-8: b'{"\xe5\xa4\x87\xe6\xb3\xa8": ...}'  GBK: b'{"\xb1\xb8\xd7\xa2": ...}'
- PS7 实测 Get-Content 默认就是 utf-8，-Encoding utf8 可以省；写着更稳，跨 PS5.1 用得上。
- open().write() 不写 with：实测 write 完文件还是 0 字节，靠 CPython 引用计数在
  进程退出时兜底 close。能跑，但不是正确写法。较短的替代：
  Path('t.json').write_text(json.dumps(...), encoding='utf-8')
- 带 BOM 的 UTF-8 文件 json.load 会 JSONDecodeError: Unexpected UTF-8 BOM。
  改 encoding='utf-8-sig' 就好。utf-8-sig 的 -sig 就是「处理签名(BOM)」。
