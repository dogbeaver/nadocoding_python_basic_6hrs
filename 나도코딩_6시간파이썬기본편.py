print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자열 자료형 (00'11'45)
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋㅋ"*3)

# boolean 자료형 - 참/거짓 (00'13'15)
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))

# 변수 (00'15'14) & 주석 

'''
애완동물을
소개해
주세요~
'''

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" +animal + "의 이름은" + name + "에요")
hobby = "공놀이"
#print(name + "는" +str(age) + "살이며," + hobby + "을 아주 좋아해요")
print(name, "는", age, "살이며,",hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))

 
''' Quiz (00'24'10) 변수를 이용하여 다음 문장을 출력하시오

변수명
 : station

변수값
 : "사당", "신도림", "인천공항" 순서대로 입력

출력 문장
 : XX 행 열차가 들어오고 있습니다.
'''

v1 = "사당"
v2 = "신도림"
v3 = "인천공항"

print(v1, "행 열차가 들어오고 있습니다.")
print(v2, "행 열차가 들어오고 있습니다.")
print(v3, "행 열차가 들어오고 있습니다.")


# 연산자 (00'25'53')
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 1
print(5//3) # 몫 구하기 1 
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) #True

print(1 != 3) #같지않다 True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # or 조건에서는 둘 중 하나만 True여도 True 
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False


# 간단한 수식 (00'33'25)
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18
print(number)
number -= 2 # 16
print(number)

number %= 5 # 1 (나머지)
print(number)


# 숫자 처리 함수 (00'36'24)
print(abs(-5)) # 절대값 5
print(pow(4, 2)) # 4의 이승 4^2 = 4*4 = 16
print(max(5, 12)) # 둘 중 최댓값 (더큰수) 12
print(min(5, 12)) # 둘 중 최솟값 5

print(round(3.14)) # 반올림값 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림, 4
print(ceil(3.14)) # 올림, 4
print(sqrt(16)) # 제곱근, 4


# 랜덤 함수 (00'38'59)
from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성 / int 붙여서 정수의 값을 볼 수 있음
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성


#로또 점수 임의로 뽑을 때 설정하는 법 
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성


# Quiz (00'44'13)
''' 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3 번은 온라인으로 하고 1 번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''

from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + " 일로 선정되었습니다.")

# 문자열 (00'46'58)

 

















