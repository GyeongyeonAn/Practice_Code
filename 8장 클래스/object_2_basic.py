# 딕셔너리를 리턴하는 함수를 선언합니다.
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
        }

# 학생 리스트를 선언합니다.
students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("서상성", 87, 98, 88, 95),
    create_student("최선지", 98, 100, 89, 50),
    create_student("고수영", 87, 98, 88, 95),
    create_student("신성민", 87, 98, 88, 95),
    create_student("안경연", 100, 100, 100, 100)
    ]

# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] +\
                student["english"] + student["science"]
    score_average = score_sum / 4
    # 출력합니다.
    print(student["name"], score_sum, score_average, sep="\t")
