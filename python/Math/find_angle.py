import math

ab = float(input())
bc = float(input())

angle_rad = math.atan(ab / bc)
angle_deg = math.degrees(angle_rad)

print(f"{round(angle_deg)}{chr(176)}")