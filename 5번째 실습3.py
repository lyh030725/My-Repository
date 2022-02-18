user_in = int(input("숫자를 입력하세요: "))
nums = range(1,user_in + 1)
nums_lst = list(nums)
nums_join = "".join(nums_lst)

print(nums_join.count(1))
