# Day 2 · Python 基础（一）：变量 / 字符串 / 列表 / 字典

> 约 1.5 小时 = 45 分钟视频 + 45 分钟动手
> 产出：`code/week01/basics02.py`（今天所有练习都写在这一个文件里）

## 三条硬性要求

1. **手敲，不复制粘贴** —— 复制粘贴学不会手感
2. **先猜再跑** —— 每写一段，先猜输出是什么，再运行，看和你想的一样不一样
3. **关掉视频默写** —— 每关结束，关掉视频，凭记忆把那几行写出来

## 开工检查（1 分钟）

```powershell
conda activate agent
cd D:\work\agent-lab\code\week01
```

- [ ] 提示符是 `(D:\conda-envs\agent)`
- [ ] 在 VS Code 里新建 `basics02.py`

**怎么找视频章节**：B 站课程的分 P 标题就是章节名，直接在目录里翻关键词「变量」「字符串」「列表」「字典」。

---

## 第 1 关　变量与数据类型（10 分钟视频）

**学完必须能写出**（关掉视频）
- [ ] 整数、浮点数、字符串、布尔值，各赋值给一个变量
- [ ] 用 `type()` 打印它们的类型
- [ ] 数字相加 vs 字符串相加，看出区别

**练习 A1**　定义 4 个变量（整数 / 浮点数 / 字符串 / 布尔值），打印每个的值和类型

期望输出（类似）：
```
10 <class 'int'>
3.14 <class 'float'>
Python <class 'str'>
True <class 'bool'>
```

**练习 A2**　把 `"3"`（字符串）和 `3`（数字）相加会怎样？**先猜，再跑**，把报错抄下来。

---

## 第 2 关　字符串与 f-string（15 分钟视频）

**学完必须能写出**
- [ ] 拼接 `"a" + "b"`、重复 `"ab" * 3`
- [ ] 长度 `len(s)`
- [ ] 切片 `s[0]`、`s[0:5]`、`s[-1]`
- [ ] f-string：`f"{name} 今年 {age} 岁"`
- [ ] `.upper()` `.lower()` `.strip()` `.replace()`

**练习 B1**　`s = "Hello Python"`，打印：

| 要什么 | 期望输出 |
|---|---|
| 长度 | `11` |
| 第一个字符 | `H` |
| 前 5 个字符 | `Hello` |
| 最后一个字符 | `n` |
| 全大写 | `HELLO PYTHON` |

**练习 B2**　`name = "小明"`、`age = 18`，用 f-string 打印 `小明今年18岁`

**练习 B3**　`s = "  hello  "`，打印去掉两边空格后的结果，和去掉之前的长度

期望：
```
5
hello
```

---

## 第 3 关　列表 list（20 分钟视频）

**学完必须能写出**
- [ ] 建列表、取值、切片
- [ ] `.append()` `.insert()`
- [ ] `.remove()` / `.pop()`
- [ ] `len()`
- [ ] 遍历 `for x in lst:`
- [ ] `.sort()` `.reverse()`
- [ ] `in` 判断元素在不在

**练习 C1**　`fruits = ["apple", "banana", "orange"]`
- 打印整个列表
- 追加 `"grape"`
- 打印第一个和最后一个
- 打印长度

**练习 C2**　用 `for` 把列表每个元素打印出来，**前面带序号**
提示：`enumerate(lst, start=1)`

**练习 C3**　`nums = [5, 2, 9, 1, 7]`，打印最大值、最小值、总和，再排序后打印

期望（部分）：
```
9
1
24
[1, 2, 5, 7, 9]
```

---

## 第 4 关　字典 dict（20 分钟视频）

**学完必须能写出**
- [ ] 建字典 `{"name": "小明", "age": 18}`
- [ ] 取值 `d["name"]`、安全取值 `d.get("xxx", "默认值")`
- [ ] 新增 / 修改 `d["city"] = "天津"`
- [ ] 删除 `del d["age"]`
- [ ] 判断键在不在 `"name" in d`
- [ ] 遍历 `.items()`

**练习 D1**　建一个字典描述一个虚构人物，含 `name` / `age` / `hobby`
- 打印整个字典
- 打印 `name` 的值
- 用 `.get()` 取不存在的键 `"city"`，默认返回 `"未知"`

**练习 D2**　遍历字典，打印成 `键 = 值`：

```
name = 小明
age = 18
hobby = 写代码
```

**练习 D3**（有点挑战，做不出来可跳过）

统计字符串 `"apple banana apple orange banana apple"` 里每个词出现几次：

```
apple: 3
banana: 2
orange: 1
```

提示：`.split()` 拆成列表，再用字典累加

> **这个练习就是 Day 2 正事的核心逻辑。** 做出来说明你已经可以回去做 `wordcount.py` 了。

---

## 自测（今天最重要的一步）

**关掉所有文档和视频**，新建一个临时文件，凭记忆写：

1. 建一个列表装 5 个数字，打印总和和平均值
2. 建一个字典装 3 个键值对，遍历打印
3. 用 f-string 打印一句含变量的话

**三个都写出来 = 今天过关。** 写不出来就回去重看那一关，不用硬往下走。

---

## 参考答案（**先自己做完再看**）

### A1
```python
i = 10
f = 3.14
s = "Python"
b = True

print(i, type(i))
print(f, type(f))
print(s, type(s))
print(b, type(b))
```

### B1
```python
s = "Hello Python"
print(len(s))
print(s[0])
print(s[0:5])
print(s[-1])
print(s.upper())
```

### C1
```python
fruits = ["apple", "banana", "orange"]
print(fruits)
fruits.append("grape")
print(fruits[0], fruits[-1])
print(len(fruits))
```

### C2
```python
for n, fruit in enumerate(fruits, start=1):
    print(n, fruit)
```

### C3
```python
nums = [5, 2, 9, 1, 7]
print(max(nums))
print(min(nums))
print(sum(nums))
nums.sort()
print(nums)
```

### D1 / D2
```python
person = {"name": "小明", "age": 18, "hobby": "写代码"}

print(person)
print(person["name"])
print(person.get("city", "未知"))

for k, v in person.items():
    print(f"{k} = {v}")
```

### D3（两种写法）
```python
# 写法一：手工累加
text = "apple banana apple orange banana apple"
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1

for w, c in counts.items():
    print(f"{w}: {c}")
```

```python
# 写法二：用标准库（更专业，Day 2 会用）
from collections import Counter

text = "apple banana apple orange banana apple"
for w, c in Counter(text.split()).most_common():
    print(f"{w}: {c}")
```

---

## 常见坑

| 现象 | 原因 |
|---|---|
| `IndexError: list index out of range` | 索引超了。列表长度 3，最大索引是 **2** |
| `KeyError: 'xxx'` | 字典里没有这个键。想安全取值用 `d.get("xxx", 默认值)` |
| `TypeError: can only concatenate str...` | 字符串和数字用 `+` 拼了。用 f-string |
| `AttributeError: 'list' object has no attribute 'length'` | Python 是 `len(lst)`，不是 `lst.length()` |
| 改了 `s[0] = "X"` 报错 | **字符串不可变**，只能生成新字符串 |
| 中文引号 `“”` | Python 只认英文引号 `""` |
| `IndentationError` | 缩进不对，Python 靠缩进划分代码块 |

---

## 收工

```powershell
cd D:\work\agent-lab
git add -A
git commit -m "basics: Day 2 变量/字符串/列表/字典"
git push
```

---

## 明天预告

**Day 3：if / 循环 / 函数** —— 然后 Day 4 学文件读写和异常，就可以回去把 `wordcount.py` 做完了。