# Day 4 · Python 基础（三）：文件读写 + 异常处理

> 约 1.5 小时 = 45 分钟视频 + 45 分钟动手
> **今天是补基础的最后一天**，学完就回去做 `wordcount.py` 项目

## 开工检查

新开终端应该自动就是对的（`(D:\conda-envs\agent) PS D:\work\agent-lab\code\week01>`）。
如果不对，敲一个词：`agent`

---

## 第 8 关　文件读写（25 分钟视频）

**学完必须能写出**
- [ ] `open()` 三种模式：`"r"` 读 / `"w"` 写（**会清空原内容**）/ `"a"` 追加
- [ ] **`with open(...) as f:` 的写法**（自动关文件，永远用这个）
- [ ] `f.read()` 一次读完
- [ ] `f.readlines()` 按行读成列表
- [ ] **`for line in f:` 逐行遍历** ← 最常用
- [ ] `line.strip()` 去掉行尾的换行符 ← **必学**
- [ ] `f.write("内容\n")`
- [ ] **`encoding="utf-8"`** ← 读中文文件必须写，否则乱码

**练习 H1　数行数**

读 `sample.txt`，打印它有多少行。

期望：打印出 `sample.txt 共 X 行`
提示：`for line in f:` ＋ 计数器 `count += 1`

**练习 H2　带行号打印**

逐行打印 `sample.txt`，每行前面加行号。

期望（前 3 行）：
```
1: Large language model agents are programs...
2: 
3: The idea sounds simple...
```

**练习 H3　写文件**

把 1 到 5 写进一个新文件 `output.txt`（每行一个数字）。

然后用这条命令看写进去没有：
```powershell
Get-Content output.txt
```

> ⚠️ 如果你不小心用了 `"w"` 模式打开 `sample.txt`，**内容会被清空**！
> 写文件一定要**新建另一个文件名**，别拿重要的文件试。

**练习 H4　数单词（挑战，做不出可跳过）**

读 `sample.txt`，数一数里面出现了多少次 `agent`（不区分大小写）。

提示：
```python
for line in f:
    for word in line.lower().split():
        if word == "agent":
            count += 1
```

> 这个练习距离 `wordcount.py` 只差一步——把「数一个词」换成「数所有词」。

---

## 第 9 关　异常处理（20 分钟视频）

**学完必须能写出**
- [ ] `try: ... except: ...` 的基本结构
- [ ] 捕获**具体**异常：`except FileNotFoundError:`
- [ ] 打印错误信息：`except Exception as e:` 然后 `print(e)`
- [ ] 为什么不要只写 `except:`（会吞掉所有错误，连自己写错都发现不了）

**练习 I1　文件不存在也不崩**

写代码读一个**不存在**的文件（比如 `不存在.txt`），用 `try/except` 捕获，打印一句中文提示。

期望：打印 `文件不存在，请检查路径`，**而不是一堆红色报错**

**练习 I2　输入不是数字**

```python
num = int(input("输入一个数字："))
```
如果输入 `abc` 会怎样？**先猜，再跑**。然后用 `try/except ValueError` 处理掉。

**练习 I3　对比实验（很重要）**

故意写一句有错的代码（比如 `print(1/0)`），分别用这两种方式跑：

```python
# 方式一
try:
    print(1 / 0)
except:
    print("出错了")

# 方式二
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("出错了：", e)
```

**体会区别**：方式一你不知道到底错在哪，方式二告诉你「division by zero」。

---

## 自测（3 分钟）

**关掉所有资料**，凭记忆写：

1. 用 `with open` 打开 `sample.txt`，打印它有多少行
2. 用 `try/except` 处理「文件不存在」的情况

**写出来 = 补基础阶段全部通关。**

---

## 常见坑

| 现象 | 原因 |
|---|---|
| 中文乱码 | 没写 `encoding="utf-8"` |
| 每行输出多一个空行 | 文件内容自带 `\n`，`print` 又加了一个 → 用 `line.strip()` |
| `FileNotFoundError` | 路径不对。**相对路径是相对于"当前目录"**，用 `cd` 确认 |
| 文件内容被清空 | 用 `"w"` 模式打开了已有文件（`"w"` 会先清空再写） |
| 报错说文件被占用 | 文件正被别的程序打开（比如 Excel） |
| `IndentationError` | `try` / `except` 下面的代码要缩进 4 格 |

---

## 今天学完之后

**你已经具备把 `wordcount.py` 做完的全部语法了：**

| 项目需要 | 你在哪天学的 |
|---|---|
| 读文件、逐行遍历 | **今天（第 8 关）** |
| 统计每个词出现次数 | Day 2（`counts.get(w,0)+1`） |
| 排序、取前 N 个 | Day 2（`sorted`、切片） |
| 文件不存在时友好报错 | **今天（第 9 关）** |
| 参数解析 | Day 1（argparse） |
| 拆函数 | Day 3（`def` / `return`） |

**Day 5 就回去做项目：让 `wordcount.py` 真的能统计词频。**

---

## 收工

```powershell
cd D:\work\agent-lab
git add -A
git commit -m "basics: Day 4 文件读写/异常"
git push
```

> 判断推送成功：`git status -sb` 里**没有 `[ahead]`**。