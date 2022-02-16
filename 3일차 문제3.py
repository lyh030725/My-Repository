in_1 = int(input("첫 번째 숫자를 입력해주세요: "))
in_2 = int(input("두 번째 숫자를 입력해주세요: "))
mx = max(in_1,in_2)

def gcd(in_1,in_2):
    for i in range(1,mx+1):
        if in_1 % i == 0 and in_2 % i == 0:
            return i;
print(gcd(8,12))

