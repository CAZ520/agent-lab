# argparse 入门 · 从"为什么需要它"讲起

> 读这份之前，先把 Day 1 清单里的任务 1–4 快速跑一遍（约 20 分钟）当热身。
> 今天真正的坎，是这一份。

---

## 一、先搞清楚它解决什么问题

你写了个 `wordcount.py`，它需要知道**统计哪个文件**。这个"文件路径"从哪来？

### 笨办法 1 · 写死在代码里

```python
path = "sample.txt"
```

换个文件就要改代码。别人根本没法用你的工具。

### 笨办法 2 · 用 `input()` 让人打字

```python
path = input("请输入文件路径：")
```

能跑了，但：没法自动化（每次都要人盯着打字）、没法放进脚本批量调用、没法一次传好几个参数。

### 专业办法 · 命令行参数

```powershell
python wordcount.py sample.txt --top 10
```

程序一启动，就拿到了 `sample.txt` 和 `10`。

**所有专业工具都这么干**，你其实已经用过很多次了：

```
git commit -m "消息"
pip install numpy
pytest -q
```

### 那不用 argparse 行不行？行，但很痛苦

Python 自带一个 `sys.argv`，它就是"命令行被空格切开后的列表"：

```python
import sys
print(sys.argv)
```

跑 `python demo.py sample.txt --top 10`，得到：

```
['demo.py', 'sample.txt', '--top', '10']
```

**全是字符串。** 接下来全靠你自己：

- 判断 `sample.txt` 是文件路径还是别的
- 判断用户到底有没有写 `--top`
- 把 `"10"` 转成 `10`（字符串不能和数字比大小）
- 用户写了 `--top` 却没给值怎么办
- 用户想看用法说明，你还得手写一份 `--help`
- 参数少给了，你得自己报错

**这些加起来大概 50 行，还到处是 bug。argparse 把它变成 5 行。**

---

## 二、argparse 帮你做的四件事

| 它替你做 | 你不用做 |
|---|---|
| 自动生成 `--help` 用法说明 | 手写说明文档 |
| 自动检查必填项 | 自己判断"参数是不是少给了" |
| 自动类型转换（`type=int`） | 自己写 `int()` |
| 自动报错并以退出码 2 退出 | 自己写错误提示 |

---

## 三、固定套路（背下来，就四步）

```python
import argparse


def main() -> None:
    # ① 建一张"参数登记表"
    parser = argparse.ArgumentParser(description="一句话说明这个程序干什么")

    # ② 往表上登记参数
    parser.add_argument("path", help="要统计的文件路径（必填）")
    parser.add_argument("--top", type=int, default=20, help="显示前几个词，默认 20")

    # ③ 真正去读命令行（对不上就自动报错退出）
    args = parser.parse_args()

    # ④ 用 args.xxx 取值
    print(args.path)
    print(args.top)


if __name__ == "__main__":
    main()
```

### 心智模型（记住这个就不会晕）

| 代码 | 相当于 |
|---|---|
| `ArgumentParser(...)` | 拿一张**空白登记表** |
| `add_argument(...)` | 往表上**登记一项**：叫什么、要不要必填、什么类型、默认值、怎么解释 |
| `parse_args()` | 拿**真实的命令行**去核对这张表：缺必填项 → 报错；类型不对 → 报错；全对 → 打包成一个 `args` 对象 |
| `args.path` | 从核对结果里**取出那一项** |

**关键点**：`parse_args()` 之前的所有代码都只是"登记"，还没读参数。**登记 ≠ 读取。**

---

## 四、逐行拆解

### ① `parser = argparse.ArgumentParser(description="词频统计工具")`

创建一个解析器。`description` 就是 `--help` 开头那句话。

### ② `parser.add_argument("path", help="要统计的文本文件路径")`

- 名字**不带 `--`** → **位置参数**（positional）
  使用时直接把值写在命令里：`python wordcount.py sample.txt`
  **默认必填**，不给就报错
- `help="..."` → 出现在 `--help` 输出里的说明文字

### ③ `parser.add_argument("--top", type=int, default=20, help="显示前几个词")`

- 名字**带 `--`** → **可选参数**，使用时写 `--top 10`
- `type=int` → 自动把字符串 `"10"` 转成整数 `10`
  写了 `--top abc` 会**自动**报 `invalid int value`
- `default=20` → 用户不写 `--top` 时用它
  （如果既没写 `default` 又没传，`args.top` 会是 `None`）

### ④ `args = parser.parse_args()`

真正开始读命令行。**这一行才是"读取"，前面都是"登记"。**

### ⑤ `print(args.path)`

取值。**属性名 = 参数名去掉 `--`**：

| 登记时的名字 | 取值时写 |
|---|---|
| `path` | `args.path` |
| `--top` | `args.top` |
| `--my-name` | `args.my_name` ← 横杠变下划线 |

---

## 五、三条必须记住的规则

1. **不带 `--` 的必填，带 `--` 的可选**（可选参数一般都给 `default`）
2. **取值用属性，不是字符串**：`args.path` ✅ ｜ `args["path"]` ❌
3. **`help=` 一定要写**，否则 `--help` 输出很丑，别人看不懂你的工具

---

## 六、你的任务：写出 `wordcount.py`

**要求**：接收一个**必填的文件路径**和一个**可选的 `--top`（默认 20）**，把它们打印出来。

**输出格式**（严格照这个来，Day 5 要写测试）：

```
收到文件：sample.txt
将显示前 20 个词
```

**验收（逐条自己跑）**

- [ ] `python wordcount.py sample.txt` → 输出上面两行
- [ ] `python wordcount.py sample.txt --top 10` → 第二行变成「将显示前 10 个词」
- [ ] `python wordcount.py` → 报错 `the following arguments are required: path`
- [ ] `python wordcount.py --help` → 显示用法、参数说明、默认值
- [ ] `python wordcount.py sample.txt --top abc` → 报错 `invalid int value`

**提示**

- 位置参数叫 `path`，可选参数叫 `--top`
- 结构照抄第三节的四步套路，改名字和 help 文字就行
- 打印用 f-string：`print(f"收到文件：{args.path}")`
- **今天不需要真的读文件**，Day 2 才做

---

## 七、这个思路和你的目标（Agent）有什么关系

这个关系比你想的近：

**Agent 的"工具调用"（function calling）本质是同一件事。**

| argparse | Agent 工具定义 |
|---|---|
| `add_argument("path", help=..., type=str)` | `{"name": "read_file", "parameters": {"path": {"type": "string"}}}` |
| 给**人**看的参数说明 | 给**模型**看的参数说明 |
| 命令行传入值 | 模型生成参数 |
| `parse_args()` 校验 | 运行时校验模型输出 |

你以后写 Agent 的工具，做的就是这个：**给模型一张"参数登记表"，让它填**。

所以今天这 15 行，是 Agent 方向的第一块砖。

---

## 八、卡住了怎么办

1. 先看报错的**最后一行**，对照 Day 1 清单里的「常见报错对照表」
2. 20 分钟搞不定，把**完整报错 + 你的代码 + 你想实现什么**一起发我
3. 别在一个点上耗掉一整晚
