text = input()
result = ""
for char in text:
    if char != " " or not result.endswith(" "):
        result += char
print(result)