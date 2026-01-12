import datetime
import re

#es_path = 'vpn-mundo.github.io'
# 定义文件路径
file_path = r'C:\Users\eric\Desktop\aff_folder\vpn-mundo.github.io\index.md'

try:
    # 获取当前日期并调整时区 (+13小时)
    new_date = datetime.datetime.now() + datetime.timedelta(hours=13)
    new_date_str = new_date.strftime('%d/%m/%Y')  # 西班牙语日期格式: DD/MM/YYYY

    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 定义正则表达式匹配西班牙语日期格式 (DD/MM/YYYY)
    date_pattern = re.compile(r'\d{2}/\d{2}/\d{4}')

    # 更新特定行中的日期
    updated = False
    for i, line in enumerate(lines):
        if "Última actualización:" in line:
            print(f"Original: {line.strip()}")
            # 替换行中的日期，保留Markdown格式
            new_line = date_pattern.sub(new_date_str, line)
            lines[i] = new_line
            print(f"Actualizado: {new_line.strip()}")
            updated = True

    if not updated:
        print("No se encontró la línea 'Última actualización:' para actualizar.")

    # 写入更新后的内容
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

    print(f"Fecha actualizada a {new_date_str} en {file_path}.")

except FileNotFoundError:
    print(f"Error: El archivo {file_path} no se encontró.")
except Exception as e:
    print(f"Error inesperado: {e}")