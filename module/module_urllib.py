# urllib 모듈: URL을 다루는 라이브러리
# 인터넷 주소(URL)를 활용할 때 사용하는 라이브러리

from urllib import request # from 구문을 사용한 방법입니다. 혼동x

# urlopen() 함수로 구글의 메인 페이지를 읽습니다.
target = request.urlopen("https://google.com")
output = target.read()

# 출력합니다.
print(output)
