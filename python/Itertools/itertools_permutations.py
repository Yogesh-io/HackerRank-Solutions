from itertools import permutations

def print_permutations():
    S, k = input().split()
    k = int(k)
    sorted_S = sorted(S)

    perm_list = permutations(sorted_S, k)

    for p in perm_list:
        print("".join(p))

if __name__ == '__main__':
    print_permutations()