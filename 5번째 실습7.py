user_in = input("Input the number: ")

for i in range(len(user_in)):
    user_in[i] = user_in[len(user_in)-i-1]
print(f"number: {user_in}")