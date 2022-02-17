from random import randrange
print("Game Start!")
rand_n = randrange(1, 100)
def UPDOWN_Game():
    global rand_n
    while 1:
        n = int(input("n: "))

        if n > rand_n:
            print("Down")
        elif rand_n > n:
            print("Up")
        else:
            print("Succes!")
            break





UPDOWN_Game()