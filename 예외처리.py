# 조건문으로 예외 처리하기 isdigit() <- 숫자로만 구성된 글자인지 확인하는 함수
user_input_a = input("정수 입력> ")
if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
else:
    print("정수를 입력하지 않았습니다!")
print()

# try except 구문
try:
    number_input_b = int(input("정수 입력> "))
    print("원의 반지름:", number_input_b)
    print("원의 둘레:", 2 * 3.14 * number_input_b)
    print("원의 넓이:", 3.14 * number_input_a * number_input_b)
except:
    print("무언가 잘못되었습니다.")
print()

# 숫자로 변환되는 것들만 리스트에 넣기
list_input_a = ["52", "152", "안경연", "32", "안녕!"]

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{} 입니다.".format(list_number))
print()

# try except else 구문
try:        # 예외가 발생할 가능성이 있는 코드
    number_input_a = int(input("정수 입력> "))
except:     # 예외가 발생했을 때 실행할 코드
    print("정수를 입력하지 않았습니다!")
else:       # 예외가 발생하지 않았을 때 실행할 코드
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
print()

# finally 구문
try:
    number_input_a = int(input("정수 입력> "))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2 * 3.14 * number_input_a)
    print("원의 넓이:", 3.14 * number_input_a * number_input_a)
except:
    print("정수를 입력해달라고 했잖아요?!")
else:
    print("예외가 발생하지 않았습니다.")
finally:        # 무조건 실행할 코드
    print("일단 프로그램이 어떻게든 끝났습니다.")
print()

# 파일이 제대로 닫혔는지 확인하기
try:
    file = open("info.txt", "w")
    file.close()
except Exception as e:
    print(e)
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)
print()

# finally 구문 사용해 파일 닫기
try:
    file = open("info.txt", "w")
    예외.발생해라()
except Exception as e:
    print(e)
finally:        # finally를 사용하지 않아도 되지만, 깔끔함을 위해서 사용함.
    file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)
print()

# finally 구문으로 파일을 닫는 이유 (return이 있더라도 finally는 무조건 실행)
def test():
    print("함수의 첫줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤 입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("함수의 마지막 줄입니다.")
test()
print()

# finally 키워드 활용
def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()
write_text_file("test.txt", "안녕하세요!")

# finally 키워드 활용 2 (반복문과 사용)
print("프로그램이 실행되었습니다.")
while True:
    try:
        print("try 구문이 실행되었습니다.")
        break
    except:
        print("except 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("while의 마지막 부분입니다.")
print("프로그램이 종료되었습니다.")
