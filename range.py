# 범위 range
for i in range(5):
    print(str(i) + " = 반복 변수")
print()

for i in range(5, 10):
    print(str(i) + " = 반복 변수")
print()

for i in range(0, 10, 3):
    print(str(i) + " = 반복 변수")
print()

# 리스트에서 요소가 몇번째인지 알기
array = [273, 32, 103, 57, 52]
for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))
print()

# 반대로 반복하기
for i in range(4, 0 - 1, -1):
    print("현재 반복 변수: {}".format(i))
print()

# 반대로 반복하기2
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))
print()

# while을 사용하여 리스트 해당하는 값 제거하기
list_test = [1, 2, 1, 2]
value = 2
while value in list_test:
    list_test.remove(value)
print(list_test)
print()

# break 키워드
i = 0
while True:
    print("{}번째 반복문입니다.".format(i))
    i += 1
    input_text = input("> 종료하시겠습니까?(y): ")
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다.")
        break
print()

# continue 키워드
numbers = [5, 15, 6, 20, 7, 25]
for number in numbers:
    if number < 10:
        continue
    print(number)
print()

