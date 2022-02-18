user_in = input("문장 입력: ")
lst = []
for i in range(len(user_in)):
    lst.append(user_in[i])

def check_sum():
    while " " in lst:
        lst.remove(" ")

    print(f"전체 단어: {len(lst)}")
check_sum()

def check_unique():
    lst_set = set(lst)
    print(f"유니크 단어: {len(lst_set)}")
check_unique()