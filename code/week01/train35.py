s = "Hello Python"
d = "aoeiu"
sums = 0
for c in s:
    if c.lower() in d:
        sums += 1
print(sums)
for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)
