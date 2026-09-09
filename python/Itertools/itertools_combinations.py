from itertools import combinations

S,k= input().split()
k = int(k)

sorted_S = sorted(S)
comb_list = combinations(sorted_S,k)
for i in range(1, k + 1):
    comb_list = combinations(sorted_S, i)
    for c in comb_list:
        print("".join(c))