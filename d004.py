n = int(input())
s = "Hello "

for i in range(n):
    s += str(input())
    if i<n-1:
        s += ","

print(s+".")
