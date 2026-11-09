n = int(input())
if n <= 0:
    print("Newaliden broi bro")
else:
    a = [int(input()) for _ in range(n)]
    print("suma na chetnite:", sum(x for x in a if x % 2 == 0))
    d = [x for x in a if x % 2]
    print("naj golqmto chetno", max(d) if d else "nqma chetni bro")