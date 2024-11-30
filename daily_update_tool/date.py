import datetime
import re

file_path = r'C:\Users\eric\Desktop\aff_folder\hsiav.github.io\index.md'
new_date = datetime.datetime.now().strftime('%Y%m%d')
# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 定义一个正则表达式来匹配日期格式
date_pattern = re.compile(r'\d{4}年\d{1,2}月\d{1,2}号')

# 检查并更新日期
for i, line in enumerate(lines):
    if line.startswith("# 翻墙软体中国VPN推荐"):
        print(line)
        new_date = datetime.datetime.now()
        new_date = new_date +  datetime.timedelta(hours=13)
        new_date = new_date.strftime('%Y%m%d')
        new_date_encoded = new_date[:4]+'年'+new_date[4:6]+'月'+new_date[6:]+'号'
        # 使用正则表达式找到并替换日期
        print(new_date_encoded)
        lines[i] = date_pattern.sub(new_date_encoded, line)
        print(line)
# 检查并更新日期
with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)


##############################################


date_pattern = re.compile(r'\d{4}年\d{1,2}月\d{1,2}号')
# 生成新的日期字符串
new_date = datetime.datetime.now()
new_date = new_date +  datetime.timedelta(hours=13)
new_date = new_date.strftime('%Y%m%d')
# 检查并更新日期
for i, line in enumerate(lines):
    if line.startswith("最近更新"):
        print(line)
        new_date_encoded = new_date[:4]+'年'+new_date[4:6]+'月'+new_date[6:]+'号'
        lines[i] = date_pattern.sub(new_date_encoded, line)


with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)
#############################################



date_pattern = re.compile(r'\d{4}年\d{1,2}月\d{1,2}号')

# 检查并更新日期
for i, line in enumerate(lines):
    if line.startswith("从"):
        print(line)
        new_date = datetime.datetime.now()
        new_date = new_date +  datetime.timedelta(hours=13)
        new_date = new_date.strftime('%Y%m%d')
        new_date_encoded = new_date[:4]+'年'+new_date[4:6]+'月'+new_date[6:]+'号'
        # 使用正则表达式找到并替换日期
        print(new_date_encoded)
        lines[i] = date_pattern.sub(new_date_encoded, line)
        print(line)
# 检查并更新日期
with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)




date_pattern = re.compile(r'\d{4}年\d{1,2}月\d{1,2}号')

# 检查并更新日期
for i, line in enumerate(lines):
    print(line)
    new_date = datetime.datetime.now()
    new_date = new_date +  datetime.timedelta(hours=13)
    new_date = new_date.strftime('%Y%m%d')
    new_date_encoded = new_date[:4]+'年'+new_date[4:6]+'月'+new_date[6:]+'号'
    # 使用正则表达式找到并替换日期
    print(new_date_encoded)
    lines[i] = date_pattern.sub(new_date_encoded, line)
    print(line)
# 检查并更新日期
with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)






# date_pattern = re.compile(r'\d{1,2}月测试')

# # 检查并更新日期
# for i, line in enumerate(lines):
#     if '月测试' in line:
        
