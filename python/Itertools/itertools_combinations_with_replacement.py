from itertools import combinations_with_replacement

a, b = input().split()
b = int(b)

for combo in combinations_with_replacement(sorted(a), b):
    print("".join(combo))