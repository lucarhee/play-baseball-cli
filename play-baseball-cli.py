# @todo 기본기를 익히기 위해 필요한 환경설정을 알아보자.
# @todo 각각의 단계에서 어떤 주제를 알 수 있을지 생각해 보자.
# @todo 주제를 공부하는 환경은 jupyter notebook에서 하자. 하지만 야구 프로그램 실행은 터미널 환경에서 한다.

# 1. 임의의 숫자 3개를 얻는다. 0부터 9까지의 정수이다.
# searching: python generate random number

# 2. 이 3개의 숫자는 같은 숫자면 안 된다.
# @todo 무한루프를 쓰지 않는 방법을 생각해 보자.

# 3. 중복되는 부분을 합쳐보기.
# if 중복, while 중복 등 여러 경우가 있다.

# 4. 답을 맞추는 과정을 추가하기
# 여러 방법을 설명할 수 있다. -- 어떤 새로운 주제를 설명할 수 있는지 알아보자.
# set을 이용하면 그 숫자가 있는지 금방 알 수 있다.

# 5. 중복되는 것 합치기

# 6. 함수로 만들어서 읽기 쉽게 만들기

from random import randint

def init_game():
    number1 = randint(0, 9)

    while True:
        number2 = randint(0, 9)
        number3 = randint(0, 9)

        if number1 != number2 and number1 != number3 and number2 != number3:
            break

    target_number = '{}{}{}'.format(number1, number2, number3)
    return target_number

def play_game(target_number):
    # user input for guessing 3 numbers
    isSuccess = False
    challenges = 0

    while not isSuccess:
        challenges += 1
        guessing_number = input("3자리 번호를 입력하시오")
        states = {'Strike': 0, 'Ball': 0, 'Out': 0}

        for i in range(3):
            if guessing_number[i] in target_number:
                if guessing_number[i] == target_number[i]:
                    states['Strike'] += 1
                else:
                    states['Ball'] += 1
            else:
                states['Out'] += 1

        if states['Strike'] == 3:
            isSuccess = True
            print("정답은 {}입니다.".format(target_number))
            print("맞췄습니다. {}번만에 성공했습니다.".format(challenges))
        else:
            print("{Strike} 스트라이크 {Ball} 볼 {Out} 아웃".format(**states))

if __name__ == '__main__':
    play_game(init_game())
