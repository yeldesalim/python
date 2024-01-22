import math

length, width, height = map(int, input().split())
S = 2*(length * height) + 2*(width * height)
print(math.ceil(S/16))