K = int(input())

rooms = list(map(int, input().split()))

unique_rooms = set(rooms)

captains_room = (sum(unique_rooms) * K - sum(rooms)) // (K - 1)

print(captains_room)
