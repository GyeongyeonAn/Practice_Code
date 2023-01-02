# 튜플은 함수와 함께 많이 사용되는 자료형, 한번 결정된 요소는 변경 불가
# 리스트와 튜플의 특이한 사용
[a, b] = [10, 20]
(c, d) = (10, 20)
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print()

# 괄호가 없는 튜플
tuple_test = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

# 괄호가 없는 튜플 활용
a, b, c = 10, 20, 30
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)
print()

# 변수의 값을 교환하는 튜플
a, b = 10, 20

print("교환 전 값")
print("a:", a)
print("b:", b)
print()

a, b = b, a

print("# 교환 후 값")
print("a:", a)
print("b:", b)
print()

# 여러 개의 값 리턴하기
def test():
    return (10, 20)
a, b = test()
print("a:", a)
print("b:", b)
print()

# 튜플의 예: 몫과 나머지를 리턴하는 divmod() 함수
a, b = 97, 40
print("divmod(97, 40):", divmod(a, b))
