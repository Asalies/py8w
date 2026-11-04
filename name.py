from mimetypes import init


name = "  li   ming  "
parts = name.strip().split()
initals = "".join(p[0].upper() + "." for p in parts)
print(initals)
print(len(name.strip()),len(parts[0]))
