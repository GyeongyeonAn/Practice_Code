# 기본적인 함수
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")
print_3_times()
print()

# 매개변수의 기본
def print_n_times(value, n):
    for i in range(n):
        print(value)
print_n_times("안녕하세요", 3)
print()

# 가변 매개변수 (가변 매개변수 뒤에는 일반 매개변수가 올 수 없음.)
def print_m_times(m, *values): # 가변 매개변수는 매개변수의 개수가 유동적임.
    for i in range(m):
        for value in values:
            print(value)
        print()
print_m_times(3, "가변 매개변수", "이런것", "입니다.", "파이썬 프로그래밍!")

# 기본 매개변수 (기본 매개변수 뒤에는 일반 매개변수가 올 수 없음.)
def print_i_times(value, i=2): # 기본 매개변수는 미리 값을 설정하는 매개변수를 말함.
    for i in range(i):
        print(value)
print_i_times("기본 매개변수")
print()
print_i_times("기본 매개변수는 임의로 지정할 수도 있음.", 3)
print()

# 키워드 매개변수 (j=3과 같이 키워드를 넣어서 기본 매개변수를 구분한다.)
def print_j_times(*values, j=2):
    for i in range(j):
        for value in values:
            print(value)
        print()
print_j_times("안녕하세요", "즐거운", "파이썬 프로그래밍", j=3)

def test(a, b=10, c=100):
    print(a + b + c)

test(10, 20, 30)
test(a=10, b=100, c=200)
test(c=10, a=100, b=200)
test(10, c=200)
print()

# 범위 내부의 정수를 모두 더하는 함수
def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end+1, step):
        output += i
    return output

print("A.", sum_all(0, 100, 10))
print("B.", sum_all())
print("B.", sum_all(end=100, step=2))
print()

