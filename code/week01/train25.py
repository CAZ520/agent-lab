dicts = {"name": "小明", "age": 18}
a = dicts.get("city")
print(dicts["name"])
print(a)
for key, value in dicts.items():
    print(key + "=" + str(value))
zifu = ["apple", "banana", "apple", "orange", "banana", "apple"]

counts = {}
for w in zifu:
    counts[w] = counts.get(w, 0) + 1
    print(counts)
# 还是要注意复习一下
