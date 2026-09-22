import os
from datetime import datetime

# 输入
input_dir = "./nodes"
input_file = os.path.join(input_dir, "node.txt")

# 输出目录
output_dir = "./output"
os.makedirs(output_dir, exist_ok=True)

# 获取今天日期 YYYY‑MM‑DD
today = datetime.now().strftime("%Y-%m-%d")

# 统计output下已有多少个 日期‑*.txt，得到序号
count = 0
for fname in os.listdir(output_dir):
    if fname.startswith(f"{today}-") and fname.endswith(".txt"):
        count += 1

# 文件名：日期‑序号.txt
out_filename = f"{today}-{count+1}.txt"
output_file = os.path.join(output_dir, out_filename)

# 读取原始节点
if not os.path.exists(input_file):
    print("错误：nodes/node.txt 不存在！")
    exit(1)

with open(input_file, "r", encoding="utf-8") as f:
    raw_nodes = f.read()

# ========== 这里放你的节点处理逻辑 ==========
processed_nodes = raw_nodes
# ============================================

# 写入文件
with open(output_file, "w", encoding="utf-8") as f:
    f.write(processed_nodes)

print(f"✅处理完成，输出文件：{output_file}")