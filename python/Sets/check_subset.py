results = []
cases = int(input())
for _ in range(cases):
    n = int(input())
    A = set(map(int, input().split()))
    
    m = int(input())
    B = set(map(int, input().split()))
    
    results.append(A.issubset(B))
    
for _ in results:
    print(_)