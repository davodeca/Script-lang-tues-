a = []
x = int(input())
while x >= 0:
    a.append(x)
    x = int(input())
if not a:
    print("nqma danni bro sry")
else:
    print("suma", sum(a))
    print("dwucifreni chisla", sum(1 for y in a if 10 <= y <= 99))
    print("sredno %.2f" % (sum(a) / len(a)))