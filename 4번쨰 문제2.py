import random
rand_num1 = random.randrange(1,10)
rand_num2 = random.randrange(1,10)
rand_num3 = random.randrange(1,10)

def check_ball(user_num1,user_num2,user_num3):
    global rand_num1,rand_num2,rand_num3
    ball_num = 0
    if user_num1 == rand_num2 and user_num1 == rand_num3:
        ball_num += 2
    elif user_num1 == rand_num2 or user_num1 == rand_num3:
        ball_num += 1
    if user_num2 == rand_num1 and user_num2 == rand_num3:
        ball_num += 2
    elif user_num2 == rand_num1 or user_num2 == rand_num3:
        ball_num += 1
    if user_num3 == rand_num2 and user_num3 == rand_num1:
        ball_num += 2
    elif user_num3 == rand_num2 or user_num3 == rand_num1:
        ball_num += 1
    return ball_num

def check_strike(user_num1,user_num2,user_num3):
    global rand_num1,rand_num2,rand_num3
    strike_num = 0
    if user_num1 == rand_num1:
        strike_num += 1
    if user_num2 == rand_num2:
        strike_num += 1
    if user_num3 == rand_num3:
        strike_num += 1
    return strike_num

user_cho = input("Play game?(y,n): ")
if user_cho == "y":

    for i in range(9):
        user_num1 = int(input("1st number: "))
        user_num2 = int(input("2nd number: "))
        user_num3 = int(input("3rd number: "))
        total_check_ball = check_ball(user_num1,user_num2,user_num3)
        total_check_strike = check_strike(user_num1,user_num2,user_num3)
        if total_check_strike == 0 and total_check_ball == 0:
            print("OUT!")
        elif total_check_strike ==3:
            print("User Winner!")
        else:
            print(f"Ball: {total_check_ball}, Strike{total_check_strike} ")
    print("User Lose..")

else:
    pass