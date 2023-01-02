# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4    # self부분은 매개변수를 전달하지 않음!

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

# 학생 리스트를 선언합니다.
students = [
    Student("안경연", 100, 100, 100, 100),
    Student("안경범", 100, 98, 88, 99),
    Student("안경훈", 90, 97, 88, 87),
    Student("파이썬", 67, 31, 55, 88),
    Student("최선지", 100, 100, 100, 100)
    ]

# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))
