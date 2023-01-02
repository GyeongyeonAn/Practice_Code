# 클래스를 선언합니다.
class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수: 반드시 첫번째 매개변수로 cls를 넣어야한다.
    @classmethod
    def print(cls): # cls의 의미는 클래스 자체를 의미한다. 
        print("------ 학생 목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("-----------------------")

    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), \
                                   self.get_average())

Student("안경연", 100, 100, 100, 100)
Student("안경범", 100, 98, 88, 99)
Student("안경훈", 90, 97, 88, 87)
Student("파이썬", 67, 31, 55, 88)
Student("최선지", 100, 100, 100, 100)

Student.print()
