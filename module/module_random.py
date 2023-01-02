# random 모듈
import random
print("# random 모듈")

print("- random():", random.random()) # 0.0 <= x < 1.0 사이의 float

print("- uniform(10, 20):", random.uniform(10, 20)) # uniform(min, max) 사이의 float

# randrange(max) 0 <= x < max 사이의 x 리턴
# randrange(min, max) min <= x < max 사이의 값 리턴
print("- randrange(10)", random.randrange(10))

# choice(list): 리스트 내부의 값 중에 랜덤으로 선택합니다.
print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))

# shuffle(list): 리스트의 요소들을 랜덤하게 섞습니다.
print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))

# sample(list, k=<숫자>): 리스트의 요소중에 k개를 뽑습니다.
print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))
print()

