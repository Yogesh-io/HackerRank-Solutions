# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())

# 1. Top Pattern
for i in range(1, N, 2):
    pattern = ".|." * i
    print(pattern.center(M, '-'))

# 2. Middle WELCOME Line
print("WELCOME".center(M, '-'))

# 3. Bottom Pattern (Reverse of the Top Pattern)
for i in range(N - 2, 0, -2):
    pattern = ".|." * i
    print(pattern.center(M, '-'))
