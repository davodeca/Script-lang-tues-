a = int(input()); b = int(input())
if a <= 0 or b <= 0:
    print("bro newalidni chisla")
else:
    x, y = a, b
    while y:
        x, y = y, x % y
    print("nod:", x)
    print("nok:", a * b // x)
    print("prosti sa wzaimno" if x == 1 else "ne sa prsto waimni")