num = int(input("pishi: "))
div_count = 0  

for i in range(1, num + 1):
    if num % i == 0:
        div_count += 1 

if div_count == 2:
    print("towa chislo e prosto")
else:
    print("towa chislo ne e prosto")