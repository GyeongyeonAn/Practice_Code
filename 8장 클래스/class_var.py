# 클래스를 선언합니다.
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        # 인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        # 클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))
        
students = [
    Student("안경연", 100, 100, 100, 100),
    Student("안경범", 100, 98, 88, 99),
    Student("안경훈", 90, 97, 88, 87),
    Student("파이썬", 67, 31, 55, 88),
    Student("최선지", 100, 100, 100, 100)
    ]

print()
print("현재 생성된 총 학생 수는 {}명 입니다.".format(Student.count))
