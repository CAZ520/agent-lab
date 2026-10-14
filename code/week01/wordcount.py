import argparse
def main():
    parser =argparse.ArgumentParser(description="统计文本里每个词出现的次数")
    parser.add_argument("path",help="要统计的文本路径")
    parser.add_argument("--top",type=int,default=20,help="显示前几个词，默认20")
    args =parser.parse_args()
    print(f"收到文件：{args.path}")
    print(f"将显示前{args.top}个词")
if __name__ =="__main__":
    main()