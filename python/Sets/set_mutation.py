# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
A = set(map(int, input().split()))
N = int(input())

for n in range(N):
    operation_name = input().split()[0]
    other_set = set(map(int, input().split()))
    getattr(A, operation_name)(other_set)
print(sum(A))
