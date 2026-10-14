# 阶段 1 · 第 1 周：Python 工程化

> 每天 60–90 分钟 ｜ 共 7 天 ｜ 所有文件放在本目录
> **本周不是学语法**（你已经有 C++ 和 Python 基础），而是学"工程习惯"——
> 写出别人能跑、别人能读、你自己三个月后还能看懂的代码。

## 本周作品：命令行词频统计工具 `wordcount.py`

最终形态：

```powershell
python wordcount.py sample.txt                        # 打印词频前 20
python wordcount.py sample.txt --top 10               # 前 10
python wordcount.py sample.txt --ignore-case          # 忽略大小写
python wordcount.py sample.txt --output report.txt    # 结果写到文件
python wordcount.py --help                            # 用法说明
```

**每天固定动作（3 分钟）**

```powershell
conda activate agent
cd D:\work\agent-lab
python -c "import sys; print(sys.prefix)"    # 必须显示 D:\conda-envs\agent
```

**每天结束前**：`git add -A` → `git commit -m "..."` → `git push`

---

## Day 1　项目骨架 + 命令行参数

| | |
|---|---|
| 学 | `if __name__ == "__main__"`、函数、`argparse` |
| 写 | `wordcount.py`：接受一个文件路径参数，打印"收到文件：xxx" |
| 验收 | `python wordcount.py sample.txt` 输出 `收到文件：sample.txt`；不带参数时自动报用法错误 |
| 提交 | `week01: argparse 骨架` |

## Day 2　文件读写 + 词频统计核心

| | |
|---|---|
| 学 | `with open()`、`read()`、`split()`、`collections.Counter`、字典排序 |
| 写 | 读文件 → 分词 → 统计 → 打印前 20 名 |
| 验收 | `python wordcount.py sample.txt` 打印出真实的词频排名 |
| 提交 | `week01: 词频统计核心逻辑` |

## Day 3　异常处理 + 日志（今天开始像工程师）

| | |
|---|---|
| 学 | `try/except`、捕获**具体**异常类型、`raise`、`logging` |
| 写 | 文件不存在 → 友好提示而不是一大坨 traceback；空文件 → 明确告知；日志带时间戳 |
| 验收 | 三种场景都试一遍：正常文件 / 不存在的文件 / 空文件，输出都可读，程序不崩 |
| 提交 | `week01: 异常处理与日志` |

## Day 4　类型注解 + dataclass + 函数拆分

| | |
|---|---|
| 学 | `def f(x: int) -> str`、`list[str]`、`@dataclass`、把长函数拆成小函数 |
| 写 | `@dataclass class WordStat`；逻辑拆成 `load_text / clean / count / report` |
| 验收 | 装上 mypy 并跑通：`pip install mypy` → `mypy wordcount.py` 显示 `Success`；每个函数 ≤ 20 行 |
| 提交 | `week01: 类型注解与结构化` |

## Day 5　pytest 单元测试

| | |
|---|---|
| 学 | `pytest`、测试函数命名、`assert`、`tmp_path` 夹具 |
| 写 | 至少 5 个测试：空文件 / 单行 / 大小写 / 标点符号 / top N 截断 |
| 验收 | `pip install pytest` → `pytest -q` 全部通过 |
| 提交 | `week01: 补充单元测试` |

## Day 6　打包成"别人能用"的项目

| | |
|---|---|
| 学 | `requirements.txt`、README 的标准结构、`--help` 文案 |
| 写 | `README.md`（这个工具干什么 / 怎么装 / 怎么用 / 示例输出）；`requirements-dev.txt` |
| 验收 | **换一个新终端**，只按 README 的三步操作，能成功跑出结果 |
| 提交 | `week01: 补 README 与依赖说明` |

## Day 7　复盘与收尾

| | |
|---|---|
| 写 | 重构你觉得最丑的那段代码；给 `--top` 加默认值和范围校验 |
| 写 | `notes/python-工程化.md`：本周学到的东西 + **至少 3 条"我还没搞懂的问题"** |
| 验收 | 本仓库本周 ≥ 6 次提交；笔记里"还没搞懂"≥ 3 条 |
| 提交 | `week01: 完成第 1 周，复盘笔记` |

---

## 每天额外的 20 分钟数学

| 天 | 内容 |
|---|---|
| Day 1–3 | 3Blue1Brown《线性代数的本质》第 1–4 集（向量 / 线性组合 / 矩阵与线性变换 / 矩阵乘法） |
| Day 4–5 | 用 numpy 手算验证：向量点积、矩阵乘法、转置 —— 把 `A @ B` 和你的手算结果对照 |
| Day 6–7 | 概率起步：条件概率、独立性、期望（按你课本对应章节，做 3 道例题） |

**验收**：`code/week01/math_notes.md` 里有你的推导或 numpy 验证代码

---

## 卡住了怎么办（顺序不能反）

1. **自己先看 20 分钟**：读报错的**最后一行**，在关键位置 `print()` 中间值
2. **再问 AI**：一次给全三样东西 —— 完整报错 + 你的代码 + 你想实现什么
   （只贴报错不贴代码，等于让别人猜）
3. **还不行**：写进 `notes/` 的"我还没搞懂的问题"，先往下走，周末统一清

> 本周唯一的目标不是"代码完美"，而是**每天都有一次能跑的产出**。

## 参考资源

- [Python 官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/)
- [pytest 入门文档](https://docs.pytest.org/en/stable/getting-started.html)
- [argparse 教程](https://docs.python.org/zh-cn/3/howto/argparse.html)
- 3Blue1Brown《线性代数的本质》（B 站有官方账号）