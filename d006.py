n,s = map(str,input().split(" "))

if s=="km":
    print(int(n)*1000000)
elif s=="m":
    print(int(n)*1000)
else:
    print(int(n)*10)
