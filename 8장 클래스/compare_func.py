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
        return "{}\t{}\t{}".format(self.name, self.get_sum(), \
                                   self.get_average())

    def __eq__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() == value.get_sum()

    def __ne__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() <= value.get_sum()
    
# 학생 리스트를 선언합니다.
students = [
    Student("안경연", 100, 100, 100, 100),
    Student("안경범", 100, 98, 88, 99),
    Student("안경훈", 90, 97, 88, 87),
    Student("파이썬", 67, 31, 55, 88),
    Student("최선지", 100, 100, 100, 100)
    ]

# 학생을 선언합니다.
student_a = Student("안경연", 100, 100, 100, 100)
student_b = Student("안경범", 100, 98, 88, 99)

# 출력합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student)
print()

print("student_a == student_b =", student_a == student_b)
print("student_a != student_b =", student_a != student_b)
print("student_a > student_b =", student_a > student_b)
print("student_a >= student_b =", student_a >= student_b)
print("student_a < student_b =", student_a < student_b)
print("student_a <= student_b =", student_a <= student_b)
