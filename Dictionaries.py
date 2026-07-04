# Day 8
from collections import Counter

k = int(input())
rooms = list(map(int, input().split()))

room_counts = Counter(rooms)

for room, count in room_counts.items():
    if count == 1:
        print(room)
        break
