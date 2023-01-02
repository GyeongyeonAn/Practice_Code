# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4    # self부분은 매개변수를 전달하지 않음!

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), \
                                   self.get_average())

    def __eq__(self, value):
        return self.get_average() == value

    def __ne__(self, value):
        return self.get_average() != value

    def __gt__(self, value):
        return self.get_average() > value

    def __ge__(self, value):
        return self.get_average() >= value

    def __lt__(self, value):
        return self.get_average() < value

    def __le__(self, value):
        return self.get_average() <= value
    
# 학생 리스트를 선언합니다.
test = Student("A", 90, 90, 90, 90)


print("test == 90 =", test == 90)
print("test != 90 =", test != 90)
print("test > 90 =", test > 90)
print("test >= 90 =", test >= 90)
print("test < 90 =", test < 90)
print("test <= 90 =", test <= 90)
