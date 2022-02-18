n = input("n: ")
n_lst = n.split()
no_lst = []
for i in range(1,6)
    same_count = 0
    i = str(i)
    if i in n_lst:
        same_count += 1

    else:
        no_lst.append(i)

if same_count == 5:
    print("12345와 쌍둥이 입니다.")