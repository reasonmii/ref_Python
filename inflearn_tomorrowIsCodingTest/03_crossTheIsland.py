
# 문제2 : 섬으로 건너가라!

# 하루동안 탈 수 있는 인원 수
(25 + 15 * 5) * 12   # 1200

import datetime

오늘시간 = datetime.datetime.today()
대기인원 = 14000605

def solution(대기인원):
    
    일년일수 = 0
    for i in range(10, 0, -1):
        일년일수 += 2**i
    년 = (대기인원 // 1200) // 일년일수
    
    남은일수 = (대기인원 // 1200) % 일년일수
    월별일수누적값 = 0
    
    월 = 0
    for i in range(10, 0, -1):
        차감일 = 월별일수누적값
        월별일수누적값 += 2**i
        월 += 1
        if 월별일수누적값 > 남은일수:
            break
    
    일 = 남은일수 - 차감일
    
    최종남은인원 = 대기인원 % 1200
    
    시 = 최종남은인원 // 100 + 9   # 9시 이후
    
    # 00분, 15분마다 탈 수 있는 인원수누적
    출발분 = [25, 40, 55, 70, 85, 100]
    #  두 명이 같은 배에 한 번에 타야 함 : + 1 필요
    해당시간에남은인원 = 최종남은인원 % 100 + 1 
    for i in 출발분:
        if i > 해당시간에남은인원:
            분 = 출발분.index(i) * 10
            break
        
    # 최종남은 인원이 99명인 경우 다음 시간으로 넘어가야 함    
    if 최종남은인원 % 100 == 99:
        시 += 1
        분 = 0
    
    if(오늘시간.minute + 분 > 60):
        분 = 오늘시간.minute + 분 - 60
        시 += 1
    
    return f'{2020+년}년 {월}월 {일}일 {시}시 {분}분 출발'

solution(대기인원)


### 시간연산
import datetime

오늘시간 = datetime.datetime.today()
오늘시간

오늘시간.year
오늘시간.month
오늘시간.day
오늘시간.hour
오늘시간.minute
오늘시간.second
오늘시간.microsecond

# 1시간을 넘을 경우 -60 후 1시간을 더해야 함

시간 = 1
분 = 1
f'{시간:0>2}:{분:0>2}' # 01:01

'hello world'.zfill(20)  # '000000000hello world'
