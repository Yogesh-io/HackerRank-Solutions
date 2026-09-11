from itertools import product

K, M = map(int, input().split())

lists = []
for _ in range(K):
    elements = list(map(int, input().split()))[1:]
    lists.append([x**2 for x in elements])

max_modulo_sum = max(sum(combo) % M for combo in product(*lists))

print(max_modulo_sum)