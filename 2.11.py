# 리스트
list_a = [273, 32, 103, "문자열", True, False]
print(list_a[1:3])
list_a[0] = "변경"
print(list_a)
print()

# 대괄호안에 음수를 넣어 뒤에서부터 요소를 선택 가능
print(list_a[-1])
print()

# 리스트 접근 연산자를 다음과 같이 이중으로 사용 가능
print(list_a[3])
print(list_a[3][0])
print(list_a[3][2])
print()

# 리스트 안에 리스트를 사용 가능
list_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_b[1])
print(list_b[1][1])
print()

# 리스트 연산자: 연결(+), 반복(*), len()
li_a = [1, 2, 3]
li_b = [4, 5, 6]
print("li_a + li_b =", li_a + li_b)
print("li_a * 3 =", li_a * 3)
print("len(li_a) =", len(li_a))
print()

# 리스트에 요소 추가하기: append, insert, expend
print("append 뒤에 요소 추가하기")
li_a.append(4)
li_a.append(5)
print(li_a)
print("insert 중간에 요소 추가하기")
li_a.insert(0, "시작")
print(li_a)
print("extend 여러개 요소 뒤에 추가하기")
li_a.extend([7, 8, 9])
print(li_a)
print()

# 인덱스로 제거하기: del, pop
print("li_a:", li_a)
del li_a[1]
print("del li_a[1]:", li_a)
del li_a[:3]
print("del li_a[:3]:", li_a)
li_a.pop(2)
print("li_a.pop(2):", li_a)
li_a.pop()
print("li_a.pop():", li_a)
print()

# 값으로 제거하기: remove 단, 값이 중복인것이 있는 경우 앞에 있는 것을 제거함
li_a.remove(8)
print("li_a.remove(8):", li_a)
print()

# 모두 제거하기: clear
li_a.clear()
print("li_a.clear():", li_a)
print()

# 리스트 내부에 있는지 확인하기: in, not in 연산자
print(273 in list_a)
print("변경" in list_a)
print(273 not in list_a)
print()

# 반복문: for
for element in list_b:
    print(element)
