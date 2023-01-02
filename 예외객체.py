# 예외 객체 Exception
try:
    number_input_a = int(input("정수입력> "))

    print("원의 반지름:", number_input_a)
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:", exception)
print()

# 여러가지 예외가 발생할 수 있는 코드
list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as e:
    print("type(exception):", type(e))
    print("exception:", e)
print()
        
# 예외 구분하기
try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해주세요!")
except IndexError:
    print("리스트의 인덱스를 벗어났어요!")
print()

# 예외구문과 예외객체
try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as e:
    print("정수를 입력해주세요!")
    print(e)
except IndexError as e:
    print("리스트의 인덱스를 벗어났어요!")
    print(e)
print()

# 모든 예외 잡기
try:
    number_input = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
    예외.발생시켜주세요()
except ValueError as e:
    print("정수를 입력해주세요!")
    print(e)
except IndexError as e:
    print("리스트의 인덱스를 벗어났어요!")
    print(e)
except Exception as e:
    print("미리 파악하지 못한 에러가 발생했어요!")
    print(e)
print()
