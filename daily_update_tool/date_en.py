import datetime
import re

# 網站資料夾已改成英文版域名
# 原: vpn-mundo.github.io
# 新: VPNuniverse.github.io (請根據實際資料夾名稱調整)

file_path = r'C:\Users\eric\Desktop\aff_folder\VPNuniverse.github.io\index.md'

try:
    # 取得目前時間並加上 13 小時時區調整（與你測速圖一致）
    current_time = datetime.datetime.now() + datetime.timedelta(hours=13)
    
    # 美國常見日期格式：Month DD, YYYY (例如 January 12, 2026)
    # 也可以用 MM/DD/YYYY 格式，下面兩種都示範了
    
    # 選項1：完整英文月份名稱 (推薦用在網站比較美觀)
    month_name = current_time.strftime('%B')  # January, February, ...
    day = current_time.strftime('%d')
    year = current_time.strftime('%Y')
    new_date_str = f"{month_name} {int(day)}, {year}"   # January 12, 2026
    
    # 選項2：純數字 MM/DD/YYYY 格式（如果你比較喜歡這種）
    # new_date_str = current_time.strftime('%m/%d/%Y')   # 01/12/2026

    # 讀取檔案內容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 正則表達式：匹配常見日期格式（支援多種可能）
    # 這裡同時支援 DD/MM/YYYY, MM/DD/YYYY, Month DD, YYYY 等
    date_pattern = re.compile(r'(\d{1,2}/\d{1,2}/\d{4})|([A-Za-z]+\s+\d{1,2},\s+\d{4})')

    # 更新特定行
    updated = False
    for i, line in enumerate(lines):
        # 判斷是否為更新日期的行（英文版）
        if any(keyword in line.lower() for keyword in [
            "last updated:", 
            "last update:", 
            "updated on:", 
            "última actualización:"  # 保留舊版以防萬一
        ]):
            print(f"Original line: {line.strip()}")
            
            # 替換找到的日期部分
            new_line = date_pattern.sub(new_date_str, line)
            lines[i] = new_line
            print(f"Updated to:   {new_line.strip()}")
            updated = True

    if not updated:
        print("未找到包含 'Last updated:' 或類似關鍵字的行，無法自動更新。")
        print("請確認 index.md 中是否有類似以下文字：")
        print("Last updated: MM/DD/YYYY")
        print("或")
        print("Last updated: January 12, 2026")

    # 寫回檔案
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

    print(f"\n日期已成功更新為：{new_date_str}")
    print(f"檔案位置：{file_path}")

except FileNotFoundError:
    print(f"錯誤：找不到檔案 {file_path}")
    print("請確認資料夾名稱是否已改為 VPNuniverse.github.io")
    print("或是檔案路徑是否正確")

except Exception as e:
    print(f"發生未預期的錯誤：{e}")