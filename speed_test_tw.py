import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os
from datetime import datetime, timedelta

# 設置字體支持繁體中文
matplotlib.rc('font', family='Microsoft JhengHei')
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)

# 生成日期範圍的函數
def generate_date_range(delay):
    end_date = datetime.today() + timedelta(hours=13)
    start_date = end_date - timedelta(days=delay)
    return f"{end_date.year} {start_date.month:02d}/{start_date.day:02d}-{end_date.month:02d}/{end_date.day:02d}"

# 加載圖片的函數
def get_image(path, zoom=0.3):
    if os.path.exists(path):
        try:
            return OffsetImage(plt.imread(path), zoom=zoom)
        except Exception as e:
            print(f"圖片加載失敗 {path}: {e}")
            return None
    else:
        print(f"圖片不存在: {path}")
        return None

# VPN數據和圖片路徑
vpn_data = {
    "StrongVPN": [99, 71],
    "ExpressVPN": [84, 15],
    "Surfshark": [81, 6],
    "FlowVPN": [76, 4.7]
}
images = {
    "StrongVPN": "small/strong.jpg",  # 請確保這些路徑正確
    "ExpressVPN": "small/expressvpn.jpg",
    "Surfshark": "small/surfshark.jpg",
    "FlowVPN": "small/flowvpn.jpg"
}

# --- Plot: 四個子圖 ---
fig, axs = plt.subplots(2, 2, figsize=(15, 12))
x = [0, 1, 2, 3]  # 調整x軸刻度為連續整數，與VPN數量對應
y = [80, 100, 70, 65]
z = [50, 60, 40, 42]
vpn_names = list(vpn_data.keys())

for i, delay in enumerate([7, 14, 30, 90]):
    row, col = divmod(i, 2)
    ax = axs[row, col]
    
    # 繪製散點圖和誤差線
    ax.scatter(x, y, label="下載速度", s=100)
    ax.scatter(x, z, label="上傳速度", s=100)
    c = [3 + np.random.randint(10) for _ in range(4)]
    ax.errorbar(x, y, yerr=c, fmt="o")
    ax.errorbar(x, z, yerr=c, fmt="o")
    
    # 設置x軸刻度和標籤
    ax.set_xticks(x)
    ax.set_xticklabels(vpn_names, fontsize=10)  # 顯示VPN名稱作為文字標籤
    
    # 在x軸添加圖片
    for j, vpn_name in enumerate(vpn_names):
        imagebox = get_image(images[vpn_name], zoom=0.3)  # 調整zoom以確保圖片可見
        if imagebox:
            ab = AnnotationBbox(imagebox, (j, -10), frameon=False, xycoords='data', boxcoords="offset points", pad=0)
            ax.add_artist(ab)
    
    # 設置y軸範圍以避免圖片被遮擋
    ax.set_ylim(-20, max(y) + 20)
    
    # 設置標籤和標題
    ax.set_xlabel('VPN', fontsize=12)
    ax.set_ylabel('速度 (Mbps)', fontsize=12)
    ax.set_title(f'牆宇宙 {generate_date_range(delay)} VPN 速度評測', fontsize=14)
    ax.legend(fontsize=10)

plt.tight_layout()
plt.savefig(r"C:\Users\eric\Desktop\aff_folder\hsiav.github.io\tw\image\speed_test\vpn_speed_test_combined.png")
plt.close()

# 打印日期範圍（測試用）
for delay in [7, 14, 30, 90]:
    print(generate_date_range(delay))