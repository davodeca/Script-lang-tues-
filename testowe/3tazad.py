n = int(input())
while n <= 0:
    n = int(input())
s = str(n)
print("suma na cifrite", sum(int(c) for c in s))
print("obratnoto", int(s[::-1]))
print("palindron" if s == s[::-1] else "ne e palindorm")