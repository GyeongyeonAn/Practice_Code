# 딕셔너리 키를 기반으로 값을 저장하는 변수
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
    }
print("name:", dictionary["name"])
print("type:", dictionary["type"])
print("ingredient:", dictionary["ingredient"])
print("origin:", dictionary["origin"])
dictionary["name"] = "8D 건조 망고"
print("수정 name:", dictionary["name"])
print("dictionary[ingredient][1] =", dictionary["ingredient"][1])
print()

# 딕셔너리에 값 추가와 삭제
dictionary["price"] = 5000
del dictionary["origin"]
print(dictionary)
print()

# in 키워드: 키가 딕셔너리에 존재하는지 확인하기
key = input("> 접근하고자 하는 키: ")
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")
print()

# 딕셔너리 반복문 사용
for key in dictionary:
    print(key, ":", dictionary[key])
print()

# 딕셔너리의 리스트, 숫자를 문자열로 바꾸기 str(), 문자열의 연결 활용 문제 +연산
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1},
    {"name": "안경연", "age": 0}
    ]
print("# 우리 동네 애완동물들")
for element in pets:
    print(element["name"], str(element["age"]) + "살")
print()

# numbers에 숫자가 몇개씩 있는지 출력하는 문제
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1
print(counter)
print()

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
        },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
    }

for key in character:
    if type(character[key]) is str:
        print(key, ":", character[key])
    elif type(character[key]) is dict:
        for i in character[key]:
            print(key, ":", character[key][i])
    elif type(character[key]) is list:
        for j in character[key]:
            print(key, ":", j)
print()


