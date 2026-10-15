fruits = ["apple", "banana", "orange"]
a = fruits.copy()
a.append("grape")

print(fruits)
print(a)
print(a[0]+"和"+a[-1])
print(len(a))
for idx,item in enumerate(a,start=1):
    print(idx,item)
nums = [5, 2, 9, 1, 7]
b=max(nums)
c=min(nums)
d=sum(nums)
r=sorted(nums)
print(b)
print(c)
print(d)
print(r)



