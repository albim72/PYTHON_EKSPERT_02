from test import Test
from egzamin import Exam


print("___________property___________")
st = Test()
st.grade = 95
print(st.grade)
assert st.grade == 95

print("___________property -> z metodą statyczną___________")

st2 = Exam()
st2.writing_grade = 77
st2.math_grade = 70
print(st2.writing_grade)
print(st2.math_grade)
assert st2.writing_grade == 77
assert st2.math_grade == 70
