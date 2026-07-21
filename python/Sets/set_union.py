n = int(input())
s1 = set(map(int, input().split()))
n1 = int(input())
s2 = set(map(int, input().split()))

count = s1.union(s2)
print(len(count))
