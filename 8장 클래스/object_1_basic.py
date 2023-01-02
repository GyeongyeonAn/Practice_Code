# 학생 리스트를 선언합니다.
students = [
    {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 21},
    {"name": "연하진", "korean": 97, "math": 88, "english": 58, "science": 95},
    {"name": "구지연", "korean": 27, "math": 88, "english": 84, "science": 94},
    {"name": "나선주", "korean": 37, "math": 78, "english": 87, "science": 65},
    {"name": "윤아린", "korean": 57, "math": 68, "english": 38, "science": 45},
    {"name": "안경연", "korean": 100, "math": 100, "english": 100, "science": 100}
    ]

# 학생을 한 명씩 반복합니다.
print("이름", "총점", "평균", sep="\t")
for student in students:
    # 점수의 총합과 평균을 구합니다.
    score_sum = student["korean"] + student["math"] +\
                student["english"] + student["science"]
    score_average = score_sum / 4
    # 출력합니다.
    print(student["name"], score_sum, score_average, sep="\t")
