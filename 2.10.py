# if 조건문 ( : 콜론을 붙인다는 것!)
num = input("정수입력> ")
num = int(num)
if num > 0:
    print("양수입니다")
if num < 0:
    print("음수입니다")
if num == 0:
    print("0입니다")
print()

# 날짜/시간 출력하기
import datetime
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

# 계절 구하기

mon = now.month
if 3 <= mon <= 5:
    print("봄 입니다.")
elif 6 <= mon <= 8:
    print("여름 입니다.")
elif 9 <= mon <= 11:
    print("가을 입니다.")
else:
    print("겨울 입니다.")
print()

# pass 키워드 <- 나중에 구현하겠다는 의미로 사용
if num > 0:
    pass # 양수일 때: 아직 미구현이기 때문에 pass 사용
else:
    pass # 음수일 때: 아직 미구현이기 때문에 pass 사용

# raise NotImplementedError <- 미구현인 부분 일부러 Error가 뜨도록 만드는 구문
# 코드의 가독성을 위해 쓰임
