max = int(input())
min = max

for i in range(4):
    n = int(input())
    if n>max:
        max=n
    elif n<min:
        min=n

print(max)
print(min)
