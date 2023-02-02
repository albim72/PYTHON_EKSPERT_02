from test import Test
from egzamin import Exam
from grade import Exams
from weakgrade import ExamWeak


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

print("___________kompozycja EXAMS -> GRADE___________")
print("___________I EGZAMIN___________")
first_exam = Exams()
first_exam.writing_grade = 90
first_exam.math_grade = 65
first_exam.science_grade = 70
print(f'Pisanie - {first_exam.writing_grade} pkt')
print(f'Nauka - {first_exam.science_grade} pkt')
print(f'Liczenie - {first_exam.math_grade} pkt')

print("___________II EGZAMIN___________")
second_exam = Exams()
second_exam.writing_grade = 92
second_exam.math_grade = 34
second_exam.science_grade = 56
print(f'Pisanie - {second_exam.writing_grade} pkt')
print(f'Nauka - {second_exam.science_grade} pkt')
print(f'Liczenie - {second_exam.math_grade} pkt')

print("___________I EGZAMIN - wyniki___________")
print(f'Pisanie - {first_exam.writing_grade} pkt')
print(f'Nauka - {first_exam.science_grade} pkt')
print(f'Liczenie - {first_exam.math_grade} pkt')


print("_____________________kompozycja EXAMS -> GRADE z WeakKeyDictionary_____________________")
print("___________I EGZAMIN___________")
first_exam = ExamWeak()
first_exam.writing_grade = 90
first_exam.math_grade = 65
first_exam.science_grade = 70
print(f'Pisanie - {first_exam.writing_grade} pkt')
print(f'Nauka - {first_exam.science_grade} pkt')
print(f'Liczenie - {first_exam.math_grade} pkt')

print("___________II EGZAMIN___________")
second_exam = ExamWeak()
second_exam.writing_grade = 92
second_exam.math_grade = 34
second_exam.science_grade = 56
print(f'Pisanie - {second_exam.writing_grade} pkt')
print(f'Nauka - {second_exam.science_grade} pkt')
print(f'Liczenie - {second_exam.math_grade} pkt')

print("___________I EGZAMIN - wyniki___________")
print(f'Pisanie - {first_exam.writing_grade} pkt')
print(f'Nauka - {first_exam.science_grade} pkt')
print(f'Liczenie - {first_exam.math_grade} pkt')
