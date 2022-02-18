m = int(input("m: "))
lst = range(1, m*m+1)
out_lst = []
for i in range(m,2,-1):
    out_lst.append(lst[1+m])
    out_lst.append(lst[1