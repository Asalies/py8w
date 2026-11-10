import tools
print(tools.c_to_f(0))
print(tools.grade(75))
tools.row(5)

from tools import c_to_f, grade

print(c_to_f(37))
print(grade(59.9))
print(tools.__name__)
