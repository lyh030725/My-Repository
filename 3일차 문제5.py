from random import *

def rand_game_1():
    num1 = int(random() * 10)
    num2 = int(random() * 10)
    num3 = int(random() * 10)
    return num1,num2,num3

def check_score(num1,num2,num3):

    this_game_score = 0
    jp = 0

    if num1 == num2 == num3 == 7:
        this_game_score += 5
        jp += 1
    elif num1 == num2 == num3:
        this_game_score += 2
    elif num1 == num2 or num2 == num3 or num1 == num3:
        this_game_score += 1
    else:
        this_game_score += 0

    return this_game_score, jp



while 1:
    total_score = 0
    total_jp_num = 0
    num1,num2,num3 = rand_game_1()

    aa,jp_num = check_score(num1,num2,num3)
    total_score += aa
    total_jp_num += jp_num
    print(f"뽑힌 숫자 {num1}, {num2}, {num3}")

    cho = input("게임을 그만하시겠습니까?(y or n): ")

    if cho == "y":
        print(f"당신의 점수는 {total_score}이고, 잭팟 횟수는 {total_jp_num}입니다.")
        break

