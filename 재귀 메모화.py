min_sitable = 2
max_sitable = 10
people = 100
memo = {}

def func(remain_people, sit_people):

    key = str([remain_people, sit_people])

    #종료 조건
    if key in memo:
        return memo[key]
    if remain_people < 0:
        return 0            #무효이므로 0을 리턴
    if remain_people == 0:
        return 1            #유효하므로 수를 세기 위해 1을 리턴

    #재귀 처리
    count = 0
    for i in range(sit_people, max_sitable + 1):
         count += func(remain_people - i, i)
    #메모화 처리
    memo[key] = count
    #종료
    return count

print(func(people, min_sitable))
