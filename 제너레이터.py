# 제너레이터 함수
def test():
    print("함수가 호출되었습니다.")
    yield "test"

print("A지점 통과")
test()
print("B지점 통과")
test()
print(test())
# 제너레이터 함수는 제너레이터를 리턴함. next() 함수를 사용해야 됨.

# 제너레이터 객체와 next() 함수
def test_2():
    print("A지점 통과")
    yield 1
    print("B지점 통과")
    yield 2
    print("C지점 통과")

output = test_2()
print("D지점 통과")
a = next(output)
print(a)
print("E지점 통과")
b = next(output)
print(b)
print("F지점 통과")
c = next(output)
print(c)

next(output)
