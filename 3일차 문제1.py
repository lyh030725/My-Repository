x = int(input("x좌표를 입력하세요: "))
y = int(input("y좌표를 입력하세요: "))
if x > 0 and y > 0:
    print(f"<{x},{y}>는 1사분면에 속합니다.")
else:
    print(f"<{x},{y}>는 1사분면에 속하지 않습니다.")
if x < 0 and y > 0:
    print(f"<{x},{y}>는 2사분면에 속합니다.")
else:
    print(f"<{x},{y}>는 2사분면에 속하지 않습니다.")
if x < 0 and y < 0:
    print("f<{x},{y}>는 3사분면에 속합니다.")
else:
    print(f"<{x},{y}>는 3사분면에 속하지 않습니다.")
if x > 0 and y < 0:
    print(f"<{x},{y}>는 4사분면에 속합니다.")
else:
    print(f"<{x},{y}>는 4사분면에 속하지 않습니다.")