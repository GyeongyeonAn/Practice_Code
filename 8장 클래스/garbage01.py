# 가비지 컬렉터: 더 사용할 가능성이 없는 데이터를 메모리에서 제거하는 역할
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다.".format(self.name))
    def __del__(self):
        print("{} - 파괴되었습니다.".format(self.name))

# D를 제외하고 나머지 클래스 생성자들은 변수에 넣지 않음.
Test("A")
Test("B")
Test("C")
name = Test("D")

# 변수에 지정하지 않으면, 가비지 컬렉터는 사용하지 않겠다고 판단하고 지워버림.
