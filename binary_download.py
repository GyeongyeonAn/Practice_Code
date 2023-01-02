from urllib import request

target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

# write binary[바이너리 쓰기] 모드로
file = open("output.png", "wb")
file.write(output)
file.close()
