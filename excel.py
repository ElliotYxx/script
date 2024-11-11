import pandas as pd
import os

# 读取 Excel 文件
excel_file_path = '~/Downloads/pkgSellingRule.xlsx'  # 请替换为你的 Excel 文件路径
df = pd.read_excel(excel_file_path)

# 提取第一列数据
first_column_data = df.iloc[:, 0]  # 选择第一列

# 将数据合并成一行，并用逗号分隔
combined_data = ','.join(first_column_data.astype(str))

# 输出到 TXT 文件
output_file_path = '/Users/elliot/Downloads/output.txt'  # 输出文件路径
output_dir = os.path.dirname(os.path.expanduser(output_file_path))  # 获取输出目录

# 检查目录是否存在，如果不存在则创建
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write(combined_data)

print("数据已成功合并并输出到 output.txt 文件中。")
