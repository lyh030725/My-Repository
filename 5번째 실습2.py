print("끝말잇기 게임을 시작합니다.")
words = []
one = input("첫 단어를 말해주세요: ")
words.append(one)
i = 0
while 1:
    print("->".join(words))
    next = input("다음 단어를 말해주세요: ")
    words.append(next)

    if words[i][-1] != words[i+1][0]:
        print("끝말이 일치하지 않습니다!")
        break
    i += 1
