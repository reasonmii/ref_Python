
# 문제4 : 자리를 양보해가며!

동물 = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']

'''
1회 : ['척추동물']         # False
2회 : ['척추동물','어류']  # False
3회 : ['어류','척추동물']  # Hit
4회 : ['어류','척추동물','무척추동물']   # False
5회 : ['척추동물','무척추동물','파충류'] # False
6회 : ['무척추동물','파충류','척추동물'] # Hit
7회 : ['파충류','척추동물','어류']      # False
8회 : ['척추동물','어류','파충류']      # Hit
'''

def solution(동물, 자리):
    의자 = [] * 자리
    
    answer = 0
    
    for i in 동물:
        if len(의자) < 3:
            # 같은 종류의 동물이 이미 의자에 앉아 있을 때
            if i in 의자:
                # 이미 같은 종이 있는 경우,
                # 해당 종을 기존 의자에서 없애서
                # 다시 맨 앞으로 넣어줌
                히트된동물 = 의자.pop(의자.index(i))
                의자.append(히트된동물)
                answer += 1
            else:
                # 같은 종이 없는 경우 바로 앉으면 됨
                의자.append(i)
                answer += 60
        else:
             # 같은 종류의 동물이 이미 의자에 앉아 있을 때
            if i in 의자:
                # 가장 마지막 동물을 없애서 다시 앞으로 넣어줌
                히트된동물 = 의자.pop(의자.index(i))
                의자.append(히트된동물)
                answer += 1
            else:
                # 최근에 Hit된 적이 없는 동물 제거 : 0번째
                의자.pop(0)
                의자.append(i)
                answer += 60           
    
    return f'{answer//60}분 {answer%60}초'
    
solution(동물, 3)
