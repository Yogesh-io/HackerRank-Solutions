def solve():
    m_size = int(input())
    set_a = set(map(int, input().split()))
    
    n_size = int(input())
    set_b = set(map(int, input().split()))
    
    sym_diff = set_a.symmetric_difference(set_b)
    sorted_result = sorted(sym_diff)
    
    for num in sorted_result:
        print(num)

if __name__ == "__main__":
    solve()