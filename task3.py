text = input().split(" ")
steps = int(input())
if steps >= 0:
    for i in range(steps):
        text.append(text.pop(0))
else:
    steps *= -1
    for i in range(steps):
        text.insert(0, text.pop())
print(text)
