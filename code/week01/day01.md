# Day 1（降低版）· 从零写出第一个 Python 脚本

> 约 70 分钟 ｜ 环境：`conda activate agent`
> **今天不碰 `argparse`**（挪到明天）。今天只求一件事：**自己写、自己跑通。**

## 今天的成果

- [ ] `hello.py` —— 打印三行
- [ ] `var.py` —— 变量和 f-string
- [ ] `func.py` —— 自己定义函数
- [ ] `flow.py` —— 判断和循环
- [ ] `math_notes.md` —— 数学笔记三行
- [ ] git 提交

---

## 第 0 步　开工（3 分钟）

```powershell
conda activate agent
cd D:\work\agent-lab\code\week01
```

- [ ] 提示符是 `(D:\conda-envs\agent)`
- [ ] VS Code 左边根目录是 `agent-lab`（不是 `cpp`）
- [ ] 左边点开了 `code` → `week01`

### VS Code 操作速查

| 想干什么 | 怎么做 |
|---|---|
| 新建文件 | 在左边 `week01` 上**右键 → 新建文件** → 输名字（**要带 `.py`**） |
| 保存 | `Ctrl + S` ← **不保存的话，跑的还是旧代码** |
| 打开终端 | `` Ctrl + ` `` |
| 跑脚本 | 终端里敲 `python 文件名.py` |

---

## 任务 1（5 分钟）`hello.py`

新建 `hello.py`，敲进这 3 行：

```python
print("hello")
print("我是小明")
print(1 + 2)
```

保存 → 终端里跑：

```powershell
python hello.py
```

**期望输出**

```
hello
我是小明
3
```

- [ ] 跑出来了

> ⚠️ 两个新手坑：
> 1. `print` 必须**顶格**，前面不能有空格
> 2. 引号必须是**英文引号** `"`，不能用中文的 `“ ”`

---

## 任务 2（10 分钟）`var.py` —— 变量和 f-string

**要求**：定义两个变量（名字、年龄），用 f-string 打印一句话。

**期望输出**

```
我叫小明，今年 18 岁
```

**提示**

- 变量不用声明类型：`name = "小明"`
- f-string：字符串前面加个 `f`，里面用 `{}` 填变量 → `print(f"我叫{name}")`
- ⚠️ 字符串和数字**不能直接相加**，要 `str(age)` 转一下

- [ ] 跑出来了

---

## 任务 3（15 分钟）`func.py` —— 定义和使用函数

**要求**：写两个函数

1. `greet(name)` —— 返回 `"你好，xxx"`
2. `add(a, b)` —— 返回两数之和

然后调用它们并打印。

**期望输出**

```
你好，小明
3 + 5 = 8
```

**提示**

- Python 函数写法：`def 函数名(参数):` ← **别忘了冒号**
- 函数体要**缩进 4 个空格**
- 返回用 `return`
- 调用：`print(greet("小明"))`

- [ ] 跑出来了

---

## 任务 4（20 分钟）`flow.py` —— 判断和循环

**要求**：
1. 给一个分数 `85`，用 `if / elif / else` 判断等级并打印
2. 用 `for` 循环打印「第 1 次」到「第 5 次」

**期望输出**

```
85 分：良好
第 1 次
第 2 次
第 3 次
第 4 次
第 5 次
```

**提示**

- `if score >= 90:` ← **别忘了冒号**，下面缩进 4 空格
- 多分支：`if ... elif ... else ...`
- 循环：`for i in range(1, 6):` 会依次得到 1、2、3、4、5（**含头不含尾**）

- [ ] 跑出来了

---

## 常见报错对照表（一定看一遍）

| 报错 | 真正原因 | 怎么改 |
|---|---|---|
| `SyntaxError: invalid syntax` | 少了冒号 `:`、括号不配对、用了中文引号 | 看**上一行**结尾有没有 `:` |
| `IndentationError: unexpected indent` | 缩进多了或乱了 | Python 靠缩进划分代码块，同一层必须对齐 |
| `NameError: name 'xxx' is not defined` | 变量名拼错或大小写错 | 检查拼写 |
| `ModuleNotFoundError` | 用错了 Python 环境 | 先 `conda activate agent` |
| `can't open file 'xxx.py'` | 当前目录不对 | `cd D:\work\agent-lab\code\week01` |
| 中文显示成乱码 | 文件编码问题 | 右下角点编码 → 选 **UTF-8** |

> 遇到任何报错：**先读最后一行**，再来这张表里找。

---

## 第 3 步　数学 20 分钟

- [ ] 看 3Blue1Brown《线性代数的本质》**第 1 集（向量）、第 2 集（线性组合 / 张成空间 / 基）**
- [ ] 新建 `math_notes.md`，写三行：
  1. 向量是什么（用你自己的话说）
  2. 什么是"线性组合"
  3. 我还没搞懂的一点

---

## 第 4 步　提交（2 分钟）

```powershell
cd D:\work\agent-lab
git add -A
git commit -m "week01: 第一个 Python 脚本"
git push
```

- [ ] GitHub 上能看到这次提交

---

## 参考答案（**先自己写**，卡住 20 分钟再看）

### `var.py`

```python
name = "小明"
age = 18
print(f"我叫{name}，今年 {age} 岁")
```

### `func.py`

```python
def greet(name):
    return f"你好，{name}"


def add(a, b):
    return a + b


print(greet("小明"))
print(f"3 + 5 = {add(3, 5)}")
```

### `flow.py`

```python
score = 85

if score >= 90:
    print(f"{score} 分：优秀")
elif score >= 80:
    print(f"{score} 分：良好")
else:
    print(f"{score} 分：继续加油")

for i in range(1, 6):
    print(f"第 {i} 次")
```

---

## 明天做什么

**Day 2 = `argparse`（就是昨天那份清单里的内容）+ 读文件。**

> 今天跨过"写文件 → 保存 → 跑出结果"这道坎，比写出 wordcount 重要得多。
