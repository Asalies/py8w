import requests
from requests.models import Response
from requests.structures import CaseInsensitiveDict
from requests.utils import get_encoding_from_headers

BODY = '{"姓名":"张三"}'.encode("gbk")
print("BODY 原始字节:", BODY)
print()

def make(content_type):
    r = Response()
    r.status_code = 200
    r._content = BODY
    r.headers = CaseInsensitiveDict({"Content-Type": content_type})
    r.encoding = get_encoding_from_headers(r.headers)
    return r

CANDIDATES = ["iso-8859-1", "latin-1", "cp1252",
              "gbk", "gb18030", "big5", "big5hkscs", "cp949",
              "utf-8", "utf-16-le"]

def is_common_han(c):
    try:
        b = c.encode("gb2312")
    except UnicodeEncodeError:
        return False
    return len(b) == 2 and 0xB0 <= b[0] <= 0xD7

def score(s):
    if "\ufffd" in s:
        return -1.0
    hans = [c for c in s if "\u4e00" <= c <= "\u9fff"]
    if not hans:
        return 0.0
    return sum(1 for c in hans if is_common_han(c)) / len(hans)

def candidates(text):
    if "\ufffd" in text:
        return [(-1.0,"-","-","含 U+FFFD，不可逆")]
    seen, out = {}, []
    for back in CANDIDATES:
        try:
            raw = text.encode(back)
        except (UnicodeEncodeError, LookupError):
            continue
        for fwd in CANDIDATES:
            if fwd == back:
                continue
            try:
                fixed = raw.decode(fwd)
            except (UnicodeDecodeError, LookupError):
                continue
            if fixed in seen:
                continue
            seen[fixed] = 1
            out.append((score(fixed), back, fwd, fixed))
    out.sort(key=lambda x: x[0], reverse=True)
    return out

for ct in ["text/html", "application/json", "text/html;charset=gbk",
           "application/octet-stream"]:
    r = make(ct)
    print("=" * 70)
    print("Content-Type :", ct)
    print("  encoding    :", repr(r.encoding))
    print("  apparent    :", repr(r.apparent_encoding))
    print("  json()      :", repr(r.json()))
    if ct=="application/json":
        print([(k, len(k)) for k in r.json()])
    print("  r.text      :", repr(r.text))
    print("  还原最可信 3 条:")
    for sc, back, fwd, fixed in candidates(r.text)[:3]:
        print(f"    压回 {back:<11} 再解 {fwd:<11} 得分 {sc:.2f}  -> {fixed!r}")
    print()
