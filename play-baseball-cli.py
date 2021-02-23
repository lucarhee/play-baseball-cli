# 1. 임의의 숫자 3개를 얻는다. 0부터 9까지의 정수이다.
# searching: python generate random number

# 2. 이 3개의 숫자는 같은 숫자면 안 된다.

from random import randint

number1 = randint(0, 9)

while True:
    number2 = randint(0, 9)

    if number2 == number1:
        continue
    else:
        break

while True:
    number3 = randint(0, 9)

    if number3 == number1 or number3 == number2:
        continue
    else:
        break

print("{}{}{}".format(number1, number2, number3))
