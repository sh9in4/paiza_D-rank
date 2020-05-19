x = int(input())
y = ""

for i in range(1,10):
    y += str(x*i)
    if i<=8:
        y += " "
print(y)
