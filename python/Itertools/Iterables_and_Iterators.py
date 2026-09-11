from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

combos = list(combinations(letters, k))

favorable = sum(1 for combo in combos if 'a' in combo)

print(f"{favorable / len(combos):.4f}")