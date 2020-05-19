m,n = map(int,input().split(" "))
s = str(m)

for i in range(9):
    s += " "
    m += n
    s += str(m)
print(s)
