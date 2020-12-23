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
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 어려워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 어려워요
"""
print(sentence3)

# 슬라이싱 (00'48'28)
ID_number = "990120-1234567"

print("성별 : " + ID_number[7])
print("연 : " +ID_number[0:2]) # 0 부터 2 직전까지 (0,1)
print("월 : " + ID_number[2:4])
print("일 : " + ID_number[4:6])

print("생년월일 : " + ID_number[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + ID_number[7:]) # 7 부터 끝까지
print("뒤 7자리 (뒤에부터) : " + ID_number[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리함수 (00'55'12)
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) #두번째 n 찾기
print(index)

print(python.find("Java")) # Java라는 단어는 없어서 -1이 나옴
''' print(python.index("Java")) # index에서는 Java라는 단어가 없으므로 오류를 냄'''
print("hi")

print(python.count("n")) #이 문장에서 n이 총 몇번 등장하는지 구할때 씀

# 문자열 포맷 (1'00'57)
''' print("a" + "b")
print("a", "b") '''

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A") # c는 character
# %s --> 다 가능
print("나느 %s살입니다." % 20)
print("나는 %s 색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))


# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")



# 탈출 문자 (1'09'17)
# \n : 줄바꿈 
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표 
# 저는 "나도코딩"입니다.
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
# print("C:\\Users\\Nadocoding\\Desktop\\Pythonworkspace>")
# 결과값 : C:\Users\Nadocoing\Desktop\Pythonworkspace>

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 지우기)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")


# Quiz 3 (1'15'50)
''' 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
                (nav)         (5)       (1)            (!)
                
예) 생성된 비밀번호 : nav51!
'''

# 내가 푼거 
rule = "http://naver.com"
print("생성된 비밀번호 : " + rule[7:])
print("생성된 비밀번호 : " + rule[7:12])
a = "naver"
print("생성된 비밀번호 : ",rule[7:10],len('naver'),len('e'),"!")

# 나도코딩이 푼거
url = "http://naver.com"
''' 예시) url = "http://daum.net" --> dau40! ''' 
my_str = url.replace("http://", "") # 규칙1
print(my_str)
my_str = my_str[:my_str.index(".")] # my_str[0:5] -->  0 ~ 5 직전까지. (0, 1, 2, 3, 4)
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))



# 리스트 [] (1'22'32) 

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈을 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)



