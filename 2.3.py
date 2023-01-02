# 정수 나누기 연산자 //
print("3 / 2 =", 3/2) 
print("3 // 2 =", 3//2)
print()

# 제곱 연산자 **
print("2 ** 1 =", 2**1)
print("2 ** 2 =", 2**2)
print("2 ** 3 =", 2**3)
print("2 ** 4 =", 2**4)
print()

# 입력 함수 input()
string = input("인사말을 입력하세요> ")
print(string)
print(type(string))
print("input에 넣은 모든 변수는 문자열 변수가 됨")
print()

# 문자열을 숫자로 바꾸기 int(), float()
str1 = "12"
print(int(str1))
print(type(str1))
print(float(str1))
print(type(str1))
print()

# 숫자를 문자열로 바꾸기 str() 
number = 12
print(str(number))
print(type(number))
number = 12.2
print(str(number))
print(type(number))
print()

# 숫자나 다양한 자료형 문자열로 변환하기 format()
format_a = "{}만원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만원 만들기".format(5000)
format_c = "{} {} {}".format(1, "문자열", True)
print(format_a)
print(format_b)
print(format_c)
print()

# 정수 출력의 format
output_a = "{:d}".format(52)
# :d는 정수를 의미
output_b = "{:5d}".format(52)
# :5d는 5칸 빈칸만들고 정수를 의미
output_c = "{:05d}".format(52)
# 5칸 빈칸에 0으로 채우고 정수를 의미
output_d = "{:05d}".format(-52)
# 5칸 빈칸에 첫번째 빈칸은 - 나머지 빈칸은 0을 채우고 정수를 의미
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print()

# format의 기호(+, -) 출력 다양한 형태
num_a = "{:+5d}".format(52)
num_b = "{:+5d}".format(-52)
num_c = "{:=+5d}".format(52)
num_d = "{:=+5d}".format(-52)
num_e = "{:+05d}".format(52)
num_f = "{:+05d}".format(-52)
print(num_a)
print(num_b)
print(num_c)
print(num_d)
print(num_e)
print(num_f)
print()

# float형 자릿수 정하기 (반올림도 자동적용됨)
f_num_a = "{:.2f}".format(52.273)
f_num_b = "{:.1f}".format(52.273)
print(f_num_a)
print(f_num_b)
print()

# float형 쓸대없는 소수점 제거하기
f_num_a = "{:g}".format(52.0)
print(f_num_a)
print()

# 문자열 양 옆 공백 제거하는 함수 strip()
st_a = """
          안녕하세요
문자열의 함수를 알아봅시다
"""
print(st_a.strip())
print()


