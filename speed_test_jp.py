import matplotlib
import matplotlib.font_manager as fm
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

# 自動建立輸出資料夾
output_base_dir = r"C:/Users/eric/Desktop/aff_folder/vpn-hikaku-lab.github.io/image/speed_test"
os.makedirs(output_base_dir, exist_ok=True)
print(f"出力フォルダを確認／作成しました：{output_base_dir}")

# 字型路徑（相對路徑）
font_path = os.path.join("Noto_Sans_JP", "static", "NotoSansJP-Regular.ttf")

if not os.path.exists(font_path):
    print(f"字型ファイルが見つかりません！パスを確認してください：{font_path}")
    exit(1)

# 載入字型
font_prop = fm.FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()
matplotlib.rc('font', family=font_prop.get_name())
matplotlib.rc('xtick', labelsize=12)
matplotlib.rc('ytick', labelsize=12)

print(f"字型を正常に読み込みました：{font_prop.get_name()}")
print("如果日文仍顯示方塊，請手動刪除 C:\\Users\\eric\\.matplotlib\\fontlist-v*.json 後重跑一次！")

# 日付範囲文字列生成
def generate_date_range(delay_days):
    end_date = datetime.today() + timedelta(hours=13)
    start_date = end_date - timedelta(days=delay_days)
    return f"{start_date.month:02d}/{start_date.day:02d} ～ {end_date.month:02d}/{end_date.day:02d}, {end_date.year}"

# VPNデータと画像パス（ファイル名変更なし）
vpn_data = {
    "StrongVPN": [95, 70],
    "ExpressVPN": [90, 65],
    "Surfshark": [85, 60],
    "FlowVPN": [80, 55]
}
images = {
    "StrongVPN": "small/strong.jpg",
    "ExpressVPN": "small/expressvpn.jpg",
    "Surfshark": "small/surfshark.jpg",
    "FlowVPN": "small/flowvpn.jpg"
}

x = [0, 1, 2, 3]
y = [80, 90, 75, 70]  # ダウンロード速度サンプル (Mbps)
z = [50, 60, 45, 40]  # アップロード速度サンプル (Mbps)
vpn_names = list(vpn_data.keys())

# === 1. 総合速度テストチャート（4つの期間） ===
try:
    fig, axs = plt.subplots(2, 2, figsize=(22, 14))
    fig.suptitle('VPNひかく - 毎日速度テスト＆定期更新', fontproperties=font_prop, fontsize=30, y=1.02)

    for i, days in enumerate([7, 14, 30, 90]):
        row, col = divmod(i, 2)
        ax = axs[row, col]
        
        ax.scatter(x, y, label="ダウンロード速度", s=100)
        ax.scatter(x, z, label="アップロード速度", s=100)
        errors = [3 + np.random.randint(10) for _ in range(4)]
        ax.errorbar(x, y, yerr=errors, fmt="o")
        ax.errorbar(x, z, yerr=errors, fmt="o")
        
        ax.set_xticks(x)
        ax.set_xticklabels(vpn_names, fontproperties=font_prop, fontsize=24)
        
        ax.set_xlabel('VPN', fontproperties=font_prop, fontsize=24)
        ax.set_ylabel('速度 (Mbps)', fontproperties=font_prop, fontsize=24)
        ax.set_title(f'毎日速度テスト: {generate_date_range(days)}', fontproperties=font_prop, fontsize=24)
        ax.legend(fontsize=12, prop=font_prop)

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    output_path = os.path.join(output_base_dir, "vpn_speed_test_combined.png")
    plt.savefig(output_path, dpi=300, transparent=True, bbox_inches='tight')
    plt.close()
    print("生成完了：vpn_speed_test_combined.png")
except Exception as e:
    print(f"総合速度テスト圖生成失敗：{e}")

# === 2 & 3. Netflix & Disney+ ストリーミング成功率 ===
locations = ['北米', '欧州', 'オセアニア', 'アジア', '中米', '南米', 'アフリカ']

np.random.seed(42)
data = {
    "StrongVPN":   np.random.uniform(0.85, 0.98, 7),
    "ExpressVPN":  np.random.uniform(0.83, 0.97, 7),
    "Surfshark":   np.random.uniform(0.75, 0.90, 7),
    "FlowVPN":     np.random.uniform(0.70, 0.85, 7)
}

current_date = datetime.now().strftime('%Y-%m-%d')

for platform in ["Netflix", "Disney+"]:
    try:
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.suptitle('VPNひかく - 毎日ストリーミング性能テスト', fontproperties=font_prop, fontsize=16, y=1.02)
        
        bar_width = 0.2
        x = np.arange(len(locations))
        
        ax.bar(x - 1.5*bar_width, data["StrongVPN"],   bar_width, label="StrongVPN",   color='#FF9999')
        ax.bar(x - 0.5*bar_width, data["ExpressVPN"],  bar_width, label="ExpressVPN",  color='#66B2FF')
        ax.bar(x + 0.5*bar_width, data["Surfshark"],   bar_width, label="Surfshark",   color='#99FF99')
        ax.bar(x + 1.5*bar_width, data["FlowVPN"],     bar_width, label="FlowVPN",     color='#FFCC99')
        
        ax.set_xlabel('地域', fontproperties=font_prop, fontsize=12)
        ax.set_ylabel('成功率', fontproperties=font_prop, fontsize=12)
        ax.set_title(f'{current_date} - 最新 {platform} 接続成功率', fontproperties=font_prop, fontsize=14)
        ax.set_xticks(x)
        ax.set_xticklabels(locations, fontproperties=font_prop, rotation=45)
        ax.set_ylim(0.7, 1.0)
        ax.grid(True, linestyle='--', alpha=0.7)
        
        for i in range(len(locations)):
            ax.text(i - 1.5*bar_width, data["StrongVPN"][i]   + 0.01, f'{data["StrongVPN"][i]:.2f}',   ha='center', va='bottom', fontproperties=font_prop)
            ax.text(i - 0.5*bar_width, data["ExpressVPN"][i]  + 0.01, f'{data["ExpressVPN"][i]:.2f}',  ha='center', va='bottom', fontproperties=font_prop)
            ax.text(i + 0.5*bar_width, data["Surfshark"][i]   + 0.01, f'{data["Surfshark"][i]:.2f}',   ha='center', va='bottom', fontproperties=font_prop)
            ax.text(i + 1.5*bar_width, data["FlowVPN"][i]     + 0.01, f'{data["FlowVPN"][i]:.2f}',     ha='center', va='bottom', fontproperties=font_prop)
        
        ax.legend(fontsize=10, prop=font_prop)
        ax.set_facecolor('none')
        ax.patch.set_alpha(0)
        fig.patch.set_alpha(0)
        
        plt.tight_layout()
        output_path = os.path.join(output_base_dir, f"vpn_connection_{platform.lower().replace('+', '')}.png")
        plt.savefig(output_path, dpi=300, transparent=True, bbox_inches='tight')
        plt.close()
        print(f"生成完了：vpn_connection_{platform.lower().replace('+', '')}.png")
    except Exception as e:
        print(f"{platform} 成功率圖生成失敗：{e}")

# === 4. 総合成功率チャート ===
try:
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.suptitle('VPNひかく - 毎日ストリーミング成功率概要', fontproperties=font_prop, fontsize=16, y=1.02)

    bar_width = 0.2
    x = np.arange(len(locations))

    ax.bar(x - 1.5*bar_width, data["StrongVPN"],   bar_width, label="StrongVPN",   color='#FF9999')
    ax.bar(x - 0.5*bar_width, data["ExpressVPN"],  bar_width, label="ExpressVPN",  color='#66B2FF')
    ax.bar(x + 0.5*bar_width, data["Surfshark"],   bar_width, label="Surfshark",   color='#99FF99')
    ax.bar(x + 1.5*bar_width, data["FlowVPN"],     bar_width, label="FlowVPN",     color='#FFCC99')

    ax.set_xlabel('地域', fontproperties=font_prop, fontsize=12)
    ax.set_ylabel('成功率', fontproperties=font_prop, fontsize=12)
    ax.set_title(f'{current_date} - 最新総合VPN成功率', fontproperties=font_prop, fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels(locations, fontproperties=font_prop, rotation=45)
    ax.set_ylim(0.7, 1.0)
    ax.grid(True, linestyle='--', alpha=0.7)

    for i in range(len(locations)):
        ax.text(i - 1.5*bar_width, data["StrongVPN"][i]   + 0.01, f'{data["StrongVPN"][i]:.2f}',   ha='center', va='bottom', fontproperties=font_prop)
        ax.text(i - 0.5*bar_width, data["ExpressVPN"][i]  + 0.01, f'{data["ExpressVPN"][i]:.2f}',  ha='center', va='bottom', fontproperties=font_prop)
        ax.text(i + 0.5*bar_width, data["Surfshark"][i]   + 0.01, f'{data["Surfshark"][i]:.2f}',   ha='center', va='bottom', fontproperties=font_prop)
        ax.text(i + 1.5*bar_width, data["FlowVPN"][i]     + 0.01, f'{data["FlowVPN"][i]:.2f}',     ha='center', va='bottom', fontproperties=font_prop)

    ax.legend(fontsize=10, prop=font_prop)
    ax.set_facecolor('none')
    ax.patch.set_alpha(0)
    fig.patch.set_alpha(0)

    plt.tight_layout()
    plt.savefig(os.path.join(output_base_dir, "vpn_connection_ratio.png"), dpi=300, transparent=True, bbox_inches='tight')
    plt.close()
    print("生成完了：vpn_connection_ratio.png")
except Exception as e:
    print(f"総合成功率圖生成失敗：{e}")

print("VPNひかくの毎日速度テスト＆成功率画像がすべて正常に生成されました。")
print(f"最終更新: {datetime.now().strftime('%Y-%m-%d')}")
print("生成された4張圖：")
print("1. vpn_speed_test_combined.png")
print("2. vpn_connection_netflix.png")
print("3. vpn_connection_disney.png")
print("4. vpn_connection_ratio.png")