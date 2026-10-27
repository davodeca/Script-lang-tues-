n = int(input())
while n > 9:
    n = sum(int(c) for c in str(n))
print(n)