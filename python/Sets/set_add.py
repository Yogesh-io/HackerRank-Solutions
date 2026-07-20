country = set()
n = int(input().strip())

for i in range(n):
    name = input().strip()
    country.add(name)
    
print(len(country))