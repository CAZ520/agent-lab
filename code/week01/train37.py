def count_vowels(s):
    sums = 0
    d = "aoeiu"
    for c in s:
        if c.lower() in d:
            sums += 1
    return sums


print(count_vowels("Hello Python"))


def greet(name, greeting="你好"):
    return f"{greeting},{name}"


print(greet("小明"))
print(greet("小明", "早上好"))
