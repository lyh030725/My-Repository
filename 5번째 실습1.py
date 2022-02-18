 f = int(input("첫 번째 사람을 입력하시오: "))
 s = int(input("두 번째 사람을 입력하시오: "))

 lst = [바위,보,가위]

if f < s and f != 0:
    print("두 번째 사람이 이겼습니다.")
elif f > s and s != 0:
    print("첫 번째 사람이 이겼습니다.")
elif f == 0 and s == 2:
    print("첫 번째 사람이 이겼습니다.")
else:
    print("두 번 째 사람이 이겼습니다.")
